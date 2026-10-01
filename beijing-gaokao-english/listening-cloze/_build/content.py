"""Three listening-memory cloze passages (about 400 words each).

Blanks are written {n:answer}; build.py turns them into numbered gaps or into
bold answers. Every passage has 10 blanks of 2-7 words, like the speech cloze it
imitates. The first passage is an original speech in the style of a diplomat's
opening remarks; the other two expand the topics of Part 2 sets 2 and 3.
"""

PASSAGES = [
    {
        "id": 1,
        "title": "访华教育代表团团长在中外青年教育对话开幕式上的讲话（节选）",
        "tag": "演讲 · 开幕致辞（原创仿写，人物与数据均为虚构）",
        "text": """
Good morning, ladies and gentlemen. I want to thank Minister Zhao and Vice Minister Liu for {1:their generous welcome and warm hospitality}. It is a great pleasure for our whole delegation to be here in Hangzhou. And it is also an honor to stand beside my colleague, Dr. Miller, and the many teachers, scientists and students who have {2:travelled thousands of miles to join this dialogue}.

I first came to China in 1998 as a young exchange student, and I have been lucky to return many times since. Every visit gives me fresh pictures of {3:a country that never stops changing}. Back in 1998, the number of students moving between our two countries was measured in the thousands. Today it is counted in {4:the hundreds of thousands}. Few classrooms back then had computers, and almost no student had an email address. Today {5:nearly every student carries a smartphone}, and a single click can bring a lecture from the other side of the world into a village school. Last night, a student from Chengdu told me she is learning to write software so that she can help doctors in her hometown. Her dream is, I think, a dream that all of us in this room share, whatever our passports say.

Now, we all know that a few days of meetings will not solve every problem in education. But we can {6:start building a framework} for learning from each other. We will not agree on every question. But we will talk about them openly, as friends and partners do.

There is a Chinese saying that a journey of a thousand miles begins with a single step. Our two countries began from very different places. China is home to {7:an ancient tradition of respecting teachers}, and this morning I saw children in the old town still bow to their teachers before class. My country is {8:a young nation built by newcomers}, and it has always learned from every corner of the world. But we know that our future, both {9:its problems and its possibilities}, will be shared.

We have walked along different roads, but that shared future is our common destination and our common duty. And, in the end, that is what this dialogue is about.

So, again, let me thank Minister Zhao and Vice Minister Liu, and I look forward to {10:three days of open and friendly discussion}. Thank you very much.
""",
        "vocab": [
            ("delegation", "代表团"), ("hospitality", "好客，款待"),
            ("exchange student", "交换生"), ("framework", "框架"),
            ("proverb / saying", "谚语"), ("destination", "目的地"),
            ("common duty", "共同的责任"), ("possibilities", "可能性，机遇"),
        ],
    },
    {
        "id": 2,
        "title": "天坛",
        "tag": "介绍 · 事物介绍类（体裁参照听力第 2 套，内容原创）",
        "text": """
Good afternoon, everyone. Today I'd like to take you to {1:one of the most famous parks in Beijing}: the Temple of Heaven. It stands in the south of the city and covers about {2:two hundred and seventy hectares}, which is much larger than the Forbidden City.

The temple has a long history. It was built in 1420, {3:during the Ming dynasty}. For nearly five hundred years, emperors came here every year to {4:pray for a good harvest}. They believed that heaven would send just the right amount of rain and sunshine, so that farmers could grow enough food for everyone. On the shortest day of winter, the emperor would walk to the Circular Mound, a three-level white stone altar, and make his offering under the open sky, with music, incense and many officials following him.

The most famous building is the Hall of Prayer for Good Harvests. It has {5:a round blue roof} with three layers, and its tall, strong wooden columns hold up the whole hall. The shapes of the buildings also carry meaning. The round roof stands for heaven, and the square walls around it stand for {6:the earth below}. In this way, the design shows the old Chinese idea that heaven and earth belong together.

Another favourite place is the Echo Wall. If you whisper to the wall from one end, a friend {7:standing at the other end} can hear your voice clearly. Visitors, especially young children, love to try it again and again.

The Temple of Heaven is also a treasure for the whole world. In 1998, it was added to {8:the UNESCO World Heritage List}, and since then, visitors from many countries have come to admire its beauty and its careful design.

Today, the park is not only a place for tourists. It is also part of daily life. Early in the morning, local residents {9:come to exercise, sing and dance} among the old cypress trees. Some practise tai chi, some play chess, and some simply sit and chat with their friends. In spring, the trees turn green, and in autumn, golden leaves fall softly on the old stone paths, so every season has its own charm.

If you ever visit Beijing, I hope you will {10:come early in the morning} and join them. You will see an ancient place that is still full of life and energy. Thank you all very much for listening.
""",
        "vocab": [
            ("harvest", "收成"), ("hectare", "公顷"), ("dynasty", "朝代"),
            ("hall", "殿，厅"), ("column", "柱子"), ("echo", "回声"),
            ("cypress", "柏树"), ("World Heritage List", "世界遗产名录"),
        ],
    },
    {
        "id": 3,
        "title": "让北京的天空重新变蓝",
        "tag": "说明 · 问题—措施类（体裁参照听力第 3 套，内容原创）",
        "text": """
Hello, everyone. Many people remember a time when winter days in Beijing were grey, and {1:the sky was hidden by thick smog}. Today I'd like to tell you how our city has been fighting for cleaner air, and what we can do to help.

First, let's look at the problem. Smog is made of tiny particles in the air, and these particles can {2:harm our lungs and hearts}. In Beijing, they came from several sources: coal burned for heating, smoke from factories, exhaust from cars and lorries, and {3:dust from building sites}. On the worst days, schools closed, flights were delayed, and people stayed indoors with their windows tightly shut.

Fortunately, the city has taken strong action. First, it changed the way people heat their homes. Millions of families {4:stopped burning coal} and switched to natural gas or electricity. Second, many old factories were closed or moved out of the city. Third, the city began to {5:control the number of cars} and encouraged people to buy electric ones. Today, many buses and taxis run on electricity, and the subway keeps {6:growing longer every year}. Fourth, the city has planted millions of trees and built new parks, because green areas can {7:catch dust and clean the air}. Fifth, builders were told to cover their sites and water the roads, so that less dust flew into the air.

These measures have worked. Over the past ten years, the amount of tiny particles in the air has fallen by more than half, and the number of blue-sky days has {8:risen year after year}. On a clear morning, many residents now enjoy {9:a beautiful view of the Western Hills}, and children can play outside without worrying about the air. Every day, the city publishes air quality data, so anyone can check the numbers on a phone before going out. I have lived here for twenty years, and I never thought I would see the hills so clearly again.

But the work is not finished. Clean air depends on all of us. You can help in simple ways: {10:take the subway or ride a bike} instead of asking for a lift, turn off the lights when you leave a room, and never burn rubbish. Small actions, repeated by millions of people, can make a big difference.

Let's keep working together, so that our grandchildren will grow up under a blue sky. Thank you for listening.
""",
        "vocab": [
            ("smog", "雾霾"), ("particle", "颗粒物"), ("exhaust", "尾气"),
            ("lorry", "卡车"), ("natural gas", "天然气"), ("subway", "地铁"),
            ("measure", "措施"), ("difference", "差别，影响"),
        ],
    },
]
