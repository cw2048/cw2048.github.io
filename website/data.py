from datetime import datetime
 
comment1 = {
    "Text" : "Sample comment",
    "Name" : "Jill",
    "Picture" : "20210812_154948.jpg",
    "Comments" : [],
    "DateTime" : datetime(2022, 5, 1, 17, 0, 0)
}

comment2 = {
    "Text" : "Sample comment again",
    "Name" : "Jack",
    "Comments" : [],
    "DateTime" : datetime(2022, 5, 1, 18, 0, 0)
}

post1 = {
    "PostId" : 1,
    "Text" : "Sample 1",
    "Name" : "Cassandra",
    "Username" : "cassandra",
    "Picture" : "20210812_154948.jpg",
    "Comments" : [comment1, comment2],
    "DateTime" : datetime(2022, 5, 1, 17, 0, 0)
}

profile = {
    "ProfileId" : 1,
    "Text" : "About me!",
    "Name" : "Cassandra",
    "Username" : "cassandra",
    "Picture" : "20210812_154948.jpg"

}

test_posts = {
    1 : post1

}

profiles = {
    1 : profile
}