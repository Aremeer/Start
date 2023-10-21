from watch import parse

def test_parse():
    assert parse('"<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"') == "https://youtu.be/xvFZjo5PgG0"
    
    assert parse('"<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"') == "https://youtu.be/xvFZjo5PgG0"
    
    assert parse('"<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"') == "https://youtu.be/xvFZjo5PgG0"
    
    
def wrong():
    assert parse('"<iframe width="560" height="315" src="https://www.twitter.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"') == None
    
    assert parse("1") == None
    
    assert parse("") == None
    
    assert parse("1234441234 asdfax") == None