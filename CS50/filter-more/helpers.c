//asked duck50 some stuff

#include "helpers.h"
#include "math.h"
#include "stdlib.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;
            int avr = round((red + green + blue) / 3.0);
            image[i][j].rgbtRed = avr;
            image[i][j].rgbtGreen = avr;
            image[i][j].rgbtBlue = avr;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++){
        int pixel_size = round(width / 2.0);
        RGBTRIPLE pixel[pixel_size];
        int rj = width - 1;
        for (int j = 0; j < round(width / 2.0); j++){
            pixel[j] = image[i][j];
            image[i][j] = image[i][rj];
            rj--;
        }
        for (int j = round(width / 2.0); j < width; j++){
            image[i][j] = pixel[rj];
            rj--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            copy[i][j] = image[i][j];
        }
    }

    for (int r = 0; r < height; r++){
        for (int c = 0; c < width; c++){
            int red = 0;
            int green = 0;
            int blue = 0;
            float counter = 0;
            for (int br = -1; br < 2; br++){
                int ir = r + br;
                for (int bc = -1; bc < 2; bc++){
                    int ic = c + bc;
                    if (ir < 0 || ir >= height || ic < 0 || ic >= width){
                        continue;
                    }
                    red += copy[ir][ic].rgbtRed;
                    green += copy[ir][ic].rgbtGreen;
                    blue += copy[ir][ic].rgbtBlue;
                    counter += 1.0;
                }
            }

            red = round(red / counter);
            green = round(green / counter);
            blue = round(blue / counter);
            image[r][c].rgbtRed = red;
            image[r][c].rgbtGreen = green;
            image[r][c].rgbtBlue = blue;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            copy[i][j] = image[i][j];
        }
    }

    for (int r = 0; r < height; r++){
        for (int c = 0; c < width; c++){
            int redx = 0;
            int greenx = 0;
            int bluex = 0;
            int redy = 0;
            int greeny = 0;
            int bluey = 0;
            float counter = 0;
            int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
            int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
            for (int br = -1; br < 2; br++){
                int ir = r + br;
                for (int bc = -1; bc < 2; bc++){
                    int ic = c + bc;
                    if (ir >= 0 && ir < height && ic >= 0 && ic < width) {
                        counter++;
                        redx += Gx[br + 1][bc + 1] * copy[ir][ic].rgbtRed;
                        greenx += Gx[br + 1][bc + 1] * copy[ir][ic].rgbtGreen;
                        bluex += Gx[br + 1][bc + 1] * copy[ir][ic].rgbtBlue;

                        redy += Gy[br + 1][bc + 1] * copy[ir][ic].rgbtRed;
                        greeny += Gy[br + 1][bc + 1] * copy[ir][ic].rgbtGreen;
                        bluey += Gy[br + 1][bc + 1] * copy[ir][ic].rgbtBlue;
                    }
                }
            }

            int red = round(sqrt(redx * redx + redy * redy));
            int green = round(sqrt(greenx * greenx + greeny * greeny));
            int blue = round(sqrt(bluex * bluex + bluey * bluey));

            if (red > 255){
                image[r][c].rgbtRed = 255;
            }
            else{
                image[r][c].rgbtRed = red;
            }

            if (green > 255){
                image[r][c].rgbtGreen = 255;
            }
            else{
                image[r][c].rgbtGreen = green;
            }

            if (blue > 255){
                image[r][c].rgbtBlue = 255;
            }
            else{
                image[r][c].rgbtBlue = blue;
            }
        }
    }
    return;
}
