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
        "title": "北京中轴线",
        "tag": "介绍 · 事物介绍类（扩写自听力第 2 套）",
        "text": """
Good afternoon, everyone. If you look at a map of Beijing, you will see {1:a straight line running from north to south}. This is the Beijing Central Axis, and it is about {2:seven point eight kilometres long}. It begins at Yongdingmen Gate in the south and ends at the Bell and Drum Towers in the north. Along it, or beside it, stand many famous places, such as Tiananmen, the Forbidden City, Jingshan Park and the Temple of Heaven.

Its history is very long. More than {3:seven hundred years ago}, when the city was planned, the builders chose a central line and placed the most important buildings along it. Later, in the Ming dynasty, the Forbidden City was completed in 1420, right {4:in the very heart of the axis}. For centuries, the city grew on both sides of this line.

The Central Axis is special for three reasons. First, its design shows the traditional Chinese idea of {5:order and balance}. Buildings stand in pairs on the left and right, and the road leads the eye from one great gate to the next. Second, it is not a museum. People still live, work and walk along it every day. In the early morning, older residents {6:practise tai chi in Jingshan Park}, and children play in the hutongs nearby. Third, it tells a long story about how a city was planned and how it has been protected. Climb Jingshan Hill and look back, and you will see rooftops spreading out on both sides of the line like a golden sea, all the way to the horizon.

Protecting the axis is not always easy. As Beijing grew quickly in the last century, some old gates were pulled down and some new buildings blocked the view. In recent years, many of those buildings have been {7:removed to open up the view}, and Yongdingmen Gate was rebuilt in 2005.

The hard work has paid off. In July 2024, the Central Axis was added to {8:the UNESCO World Heritage List}. Today, visitors from all over the world can {9:take a virtual tour online} and explore its gates, halls and gardens from home.

But I hope you will not stop there. When you have time, {10:walk along the axis yourself} from south to north, slowly, with an open mind, and feel how a great city and its daily life have grown together. Thank you very much for listening.
""",
        "vocab": [
            ("axis", "轴线"), ("dynasty", "朝代"), ("hutong", "胡同"),
            ("balance", "平衡，对称"), ("block the view", "挡住视线"),
            ("World Heritage List", "世界遗产名录"), ("virtual tour", "线上虚拟游览"),
            ("be protected", "得到保护"),
        ],
    },
    {
        "id": 3,
        "title": "北京雨燕",
        "tag": "说明 · 问题—措施类（扩写自听力第 3 套）",
        "text": """
Hello, everyone. Today I'd like to tell you about a small bird with a big connection to our city. It is called the Beijing swift, and it is {1:the only wild bird named after Beijing}. Many people know it as the bird that circles the old towers and palace roofs on summer evenings, crying out in a loud, sharp voice.

Beijing swifts are amazing flyers. They spend almost their whole lives in the air. They can eat, drink and even {2:sleep and mate while flying}. They land only when they need to build a nest and raise their young. Every spring, they come back to Beijing, and in late July they set off again for {3:the warm lands of southern Africa}. The journey is more than ten thousand kilometres in each direction.

Sadly, the number of Beijing swifts has dropped sharply. The main reason is that they are losing their homes. Swifts nest in small holes under the roofs of old buildings. But in recent years, many old buildings have been pulled down or {4:repaired and sealed up} without leaving any holes. The birds fly back from Africa and find nowhere to lay their eggs.

Fortunately, people are taking action. Scientists are studying how the swifts travel by fixing {5:tiny tracking devices to their bodies}. These devices show where the birds rest, how fast they fly, and {6:which dangers they meet on the way}. Meanwhile, volunteers are making a difference closer to home. They count the birds every summer, and they hang up special nest boxes under the eaves of old buildings and {7:in the corners of quiet parks}. Some boxes have already been used, which gives everyone hope. One volunteer told me that the first time she saw a pair of swifts enter a box, she almost cried with joy.

Schools can help too. In several districts, students {8:learn to recognise the swifts' calls} and take part in the counting. When the boxes are checked, young volunteers {9:record every egg and every chick}, so that scientists have clear data.

Protecting Beijing swifts is not only about saving one kind of bird. It is also about keeping the old city alive and {10:learning to share it with nature}. Their story reminds us that cities belong to wildlife as well. The next time you hear a sharp cry above the roofs, please look up and say hello. Thank you for listening.
""",
        "vocab": [
            ("swift", "雨燕"), ("sharply", "急剧地"), ("nest box", "人工巢箱"),
            ("tracking device", "追踪器"), ("eaves", "屋檐"),
            ("volunteer", "志愿者"), ("chick", "雏鸟"), ("recognise", "识别"),
        ],
    },
]
