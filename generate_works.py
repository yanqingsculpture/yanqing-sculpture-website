# -*- coding: utf-8 -*-
"""批量生成作品详情页"""
import os

WORKS_DIR = "works"
BASE_URL = "https://cqyqds.cn"

# ==========================================
# 作品数据
# ==========================================
works = [
    # ===== 城市雕塑 =====
    {
        "slug": "chuanzang-linggongli",
        "category": "城市雕塑",
        "category_en": "Urban Sculpture",
        "num": "N°UR-2023-001",
        "title": "川藏零公里·自驾大本营",
        "title_en": "Chuanzang Zero-Kilometer Base Camp",
        "year": "2023",
        "location": "四川雅安金鸡关",
        "location_en": "Jinjiguan, Yaan, Sichuan",
        "material": "不锈钢 · 铝板",
        "material_en": "Stainless Steel · Aluminum Plate",
        "dimensions": "《诗与远方的归途》25×15m · 《三级塔》35m",
        "dimensions_en": "Poetry & Return 25×15m · Three-Tier Tower 35m",
        "hero_img": "../images/chuanzang-linggongli.webp",
        "gallery": ["../images/chuanzang-linggongli.webp", "../images/chuanzang-sanjita.webp"],
        "intro": "2023年落成的川藏线318国道起点地标雕塑群。作品以"诗与远方的归途"为主题，将川藏公路的壮丽与自驾者的梦想凝练为雕塑语言。《三级塔》高35米，以不锈钢和铝板构筑出层层递进的视觉节奏，象征川藏线从成都平原到世界屋脊的三级地理跨越。",
        "intro_en": "A landmark sculpture group at the starting point of China National Highway 318, completed in 2023. Themed 'Poetry and the Journey Homeward', it crystallizes the grandeur of the Sichuan-Tibet Highway and the dreams of road-trippers into sculptural language. The 35-meter Three-Tier Tower, built from stainless steel and aluminum, creates a progressive visual rhythm symbolizing the three-tier geographical ascent from the Chengdu Plain to the Roof of the World.",
        "story": "金鸡关，川藏公路零公里处，千百年来是内地进藏的咽喉要道。接到这个项目时，老赵在318国道边站了整整一天，看车流、看雪山、看旅人的表情。他想的不只是一座雕塑，而是要给所有踏上这条路的人一个仪式感——从这里出发，诗与远方都在路上。",
        "story_en": "Jinjiguan, the zero-kilometer mark of the Sichuan-Tibet Highway, has been the gateway to Tibet for centuries. When commissioned for this project, Zhao spent an entire day standing by Highway 318, watching the traffic, the distant snow mountains, and the faces of travelers. What he envisioned was not just a sculpture, but a rite of passage — a point of departure where poetry and the journey ahead become one.",
    },
    {
        "slug": "daxicang",
        "category": "城市雕塑",
        "category_en": "Urban Sculpture",
        "num": "N°UR-2025-001",
        "title": "大酉藏书洞文化景区",
        "title_en": "Dayou Cangshu Cave Cultural Scenic Area",
        "year": "2025",
        "location": "湖南怀化辰溪",
        "location_en": "Chenxi, Huaihua, Hunan",
        "material": "黄砂岩 · GRC · 不锈钢 · 镀锌钢板",
        "material_en": "Yellow Sandstone · GRC · Stainless Steel · Galvanized Steel",
        "dimensions": "汉阙大门6.8m · 庄子雕塑6.8m · 106m浮雕长卷 · 共11组件",
        "dimensions_en": "Han Gate 6.8m · Zhuangzi Statue 6.8m · 106m Relief · 11 Components",
        "hero_img": "../images/daxicang-damen.webp",
        "gallery": ["../images/daxicang-damen.webp"],
        "intro": "2025年完成的大型文化雕塑群，共计11个雕塑艺术组件。以汉阙大门为序章，融合伏胜运书、庄子哲学、孔子圣像、黄帝内经竹简景墙、百家书卷等文化元素，106米浮雕长卷串联古今，呈现中华文脉的宏大叙事。",
        "intro_en": "A large-scale cultural sculpture complex completed in 2025, comprising 11 sculptural components. Opening with a monumental Han-dynasty gate (que), the project integrates cultural elements from Fusheng's book transport, Zhuangzi's philosophy, Confucius, the Yellow Emperor's Inner Canon bamboo-slip wall, and the Hundred Schools of Thought — all linked by a 106-meter relief scroll narrating China's intellectual heritage.",
        "story": "这个项目体量巨大，工期紧张，但老赵说最有意思的不是多大的门或多长的浮雕，而是伏胜运书那组雕塑——一位古代学者在战火中冒着生命危险把典籍藏进山洞。老赵觉得这跟自己把石雕技艺从学院带到宝兴深山里的经历有点像——都是在对的时间，把对的东西放在对的地方。",
        "story_en": "A massive undertaking on a tight schedule, but what fascinated Zhao most was not the monumental gate or the epic relief, but the sculpture of Fusheng transporting books — an ancient scholar hiding classical texts in a cave at the risk of his life. He saw a parallel with his own journey: bringing sculptural craftsmanship from the academy to the mountains of Baoxing — putting the right things in the right place at the right time.",
    },
    {
        "slug": "mengdingshan",
        "category": "城市雕塑",
        "category_en": "Urban Sculpture",
        "num": "N°UR-2022-001",
        "title": "蒙顶山茶诗碑林 · 茶文化公园",
        "title_en": "Mengding Mountain Tea Poetry Steles & Tea Culture Park",
        "year": "2022",
        "location": "四川雅安蒙顶山",
        "location_en": "Mengding Mountain, Yaan, Sichuan",
        "material": "水泥直塑 · 石雕 · 青石",
        "material_en": "Cement Direct Molding · Stone Carving · Bluestone",
        "dimensions": "300m茶诗碑林 · 汉阙式简介碑 3×4m",
        "dimensions_en": "300m Tea Poetry Steles · Han-Style Intro Stele 3×4m",
        "hero_img": "../images/mengdingshan-beilin.webp",
        "gallery": ["../images/mengdingshan-beilin.webp"],
        "intro": "世界茶文化发源地蒙顶山的300米茶诗碑林，将历代茶诗镌刻于水泥直塑与青石之上，辅以汉阙式简介石碑。茶诗、茶道、茶文化在此交汇，是自然山水与人文雕塑的深度融合。",
        "intro_en": "A 300-meter tea poetry stele forest at Mengding Mountain, the birthplace of world tea culture. Ancient tea poems are carved into cement and bluestone, complemented by a Han-style introductory stele. Tea poetry, ceremony, and culture converge here in a deep fusion of natural landscape and sculptural art.",
        "story": "蒙顶山是世界茶文化的源头，吴理真在此种下第一棵茶树。老赵接这个项目时想的是：怎样让雕塑"长"在茶园里，而不是"放"在茶园里。答案是用水泥直塑模拟山石的肌理，让碑林像本来就是这山的一部分。每一块碑的选址都跟着山势走，他说这叫"石刻不该抢风景的戏，应该陪风景演戏"。",
        "story_en": "Mengding Mountain is the cradle of world tea culture, where Wu Lizhen planted the first tea tree. Zhao's guiding question: How do you make a sculpture 'grow' into the tea garden rather than 'place' it there? The answer was cement direct molding to mimic native rock textures, making the stele forest feel like it had always belonged. Each stele's position follows the mountain's contours — 'Stone carving shouldn't upstage the scenery; it should perform alongside it.'",
    },
    {
        "slug": "huoche",
        "category": "城市雕塑",
        "category_en": "Urban Sculpture",
        "num": "N°UR-2017-001",
        "title": "火车拉来的城市",
        "title_en": "The City Brought by Trains",
        "year": "2017",
        "location": "贵州六盘水",
        "location_en": "Liupanshui, Guizhou",
        "material": "铸铁 · 不锈钢 · 铸铜",
        "material_en": "Cast Iron · Stainless Steel · Bronze",
        "dimensions": "铸铁320cm · 多组件",
        "dimensions_en": "Cast Iron 320cm · Multiple Components",
        "hero_img": "../images/sanxian-wamei.webp",
        "gallery": ["../images/sanxian-wamei.webp", "../images/sanxian-xiaozhen.webp"],
        "intro": "六盘水三线文化创意小镇的标志性作品。以火车为核心意象，用铸铁、不锈钢和铸铜塑造了一座城市从铁轨上"生长"出来的工业记忆，是三线建设精神的雕塑化表达。",
        "intro_en": "The signature work of Liupanshui Third-Front Cultural Creative Town. Using the train as the central motif, cast iron, stainless steel, and bronze shape the industrial memory of a city that 'grew' from the railway tracks — a sculptural expression of the Third-Front Construction spirit.",
        "story": "六盘水是一座被火车拉来的城市——三线建设时期，成千上万的人沿着铁轨来到这里，建起了煤矿和钢铁厂。老赵用铸铁做火车头，因为它沉、因为它黑、因为它有锈——这些质感本身就是这座城市的语言。",
        "story_en": "Liupanshui is a city brought by trains — during the Third-Front era, thousands arrived along these tracks to build coal mines and steel mills. Zhao chose cast iron for the locomotive because it is heavy, dark, and rusts — these textures are the city's own vocabulary.",
    },
    {
        "slug": "keji-zhiguang",
        "category": "城市雕塑",
        "category_en": "Urban Sculpture",
        "num": "N°UR-2022-002",
        "title": "科技之光 · 数据谷艺术装置",
        "title_en": "Light of Technology · Data Valley Art Installation",
        "year": "2022",
        "location": "重庆渝北数据谷",
        "location_en": "Yubei Data Valley, Chongqing",
        "material": "不锈钢",
        "material_en": "Stainless Steel",
        "dimensions": "35×8.2m",
        "dimensions_en": "35×8.2m",
        "hero_img": "../images/keji-zhiguang.webp",
        "gallery": ["../images/keji-zhiguang.webp"],
        "intro": "重庆渝北数据谷巨型不锈钢装置艺术，以数字化和科技为主题，35米跨度的流线型结构犹如数据流在空间中凝固。镜面不锈钢反射天空与城市，让雕塑成为一面与数据对话的"镜子"。",
        "intro_en": "A monumental stainless steel installation at Chongqing's Yubei Data Valley, themed on digital technology. The 35-meter streamlined structure resembles a data stream frozen in space. Mirror-polished stainless steel reflects the sky and city, turning the sculpture into a 'mirror' in dialogue with data.",
        "story": "数据谷要一个能代表"数字经济"的雕塑，老赵说数据看不见摸不着，怎么雕？后来他想到小时候看溪水流过石头——水是数据，石头是雕塑，雕塑的任务不是雕刻数据本身，而是给数据一个看得见的河道。",
        "story_en": "Data Valley wanted a sculpture representing the 'digital economy.' Zhao's challenge: How do you carve something invisible? He recalled watching streams flow over rocks as a child — the water is data, the rock is sculpture. The sculpture's role is not to carve the data itself, but to give it a visible channel.",
    },
    {
        "slug": "sanxian-wenhua",
        "category": "城市雕塑",
        "category_en": "Urban Sculpture",
        "num": "N°UR-2018-001",
        "title": "三线文化创意长廊",
        "title_en": "Third-Front Cultural Creative Corridor",
        "year": "2018",
        "location": "贵州六盘水",
        "location_en": "Liupanshui, Guizhou",
        "material": "烤盾钢 · 黄砂岩 · 铸铜 · 不锈钢",
        "material_en": "Corten Steel · Yellow Sandstone · Bronze · Stainless Steel",
        "dimensions": "系列作品群 · 最大组件800cm",
        "dimensions_en": "Series Group · Largest Component 800cm",
        "hero_img": "../images/sanxian-xuzhang.webp",
        "gallery": ["../images/sanxian-xuzhang.webp", "../images/sanxian-xinshidai.webp", "../images/sanxian-xiangji.webp"],
        "intro": "六盘水三线文化创意长廊系列雕塑群，以序章大门、开荒者、挖煤场景、炼钢炉、勘探者等十余组件，全景式再现三线建设时期的历史场景。烤盾钢的锈色与工业记忆高度契合，是工业遗产与公共艺术的典范结合。",
        "intro_en": "A sculpture series along Liupanshui's Third-Front Cultural Creative Corridor, comprising over ten components — the Prologue Gate, Pioneers, Coal Mining, Steel Furnace, Prospectors, etc. — recreating the panoramic historical scenes of the Third-Front Construction era. The rust patina of Corten steel resonates deeply with industrial memory, making this an exemplary fusion of industrial heritage and public art.",
        "story": "三线建设是老赵父亲那一辈人的集体记忆。做这个项目时他采访了很多老三线人，听他们讲当年的故事——在荒山野岭建厂房、在零下十几度挖煤。老赵说这些雕塑不是在"做历史"，而是在"翻译记忆"——把老人们嘴里的故事变成可以触摸的钢铁和石头。",
        "story_en": "The Third-Front era is the collective memory of Zhao's father's generation. He interviewed many Third-Front veterans, listening to stories of building factories in the wilderness and mining coal in sub-zero temperatures. These sculptures 'don't recreate history,' Zhao says — 'they translate memory,' turning the stories on old men's lips into steel and stone you can touch.",
    },

    # ===== 石雕创作 =====
    {
        "slug": "guanxin",
        "category": "石雕创作",
        "category_en": "Stone Sculpture",
        "num": "N°SC-2021-001",
        "title": "观·心",
        "title_en": "Guanxin · Observing the Heart",
        "year": "2021",
        "location": "",
        "location_en": "",
        "material": "鹅卵石 · 船木 · 镀锌钢管",
        "material_en": "Pebble · Boat Wood · Galvanized Steel Pipe",
        "dimensions": "可变尺寸",
        "dimensions_en": "Variable Dimensions",
        "hero_img": "../images/guanxin.webp",
        "gallery": ["../images/guanxin.webp"],
        "intro": "从河边捡回一块鹅卵石，当地人叫它'黄皮黑胆'。切开后发现两种石质共同合体。考虑它形成的原因，黑胆部分曾经是单独的存在，因为时间被泥沙包裹。一点点剥离黄色外皮，看到它原本的样子——不像外表那么圆滑，内心依然有棱有角。",
        "intro_en": "A cobblestone picked up from the riverbank, locally called 'yellow skin black gall'. Cutting it open revealed two stone types fused as one. The black gall was once a separate entity, enveloped by silt over time. Peeling away the yellow skin layer by layer unveiled its original form — unlike its smooth exterior, the interior still has edges and angles.",
        "story": "这块石头老赵在宝兴河边看到的，当地人说这叫'黄皮黑胆'，不值钱。但他觉得这块石头有意思——外表光滑圆润，里面却有棱有角。花了三个月慢慢磨掉黄皮，露出黑胆。做完那天他看着这件作品说：'这说的不就是人吗？在社会上磨得圆滑了，但心里那点棱角还在。'2023年获第十四届中轻万花杯金奖。",
        "story_en": "Zhao spotted this stone by the Baoxing River. Locals called it 'yellow skin black gall' — worthless. But he found it fascinating: smooth and rounded outside, angular within. He spent three months carefully grinding away the yellow skin to reveal the black gall. When finished, he looked at it and said: 'Isn't this what people are like? Worn smooth by society, but those edges inside — they're still there.' Won Gold at the 14th Zhongqing Wanhua Cup, 2023.",
        "award": "第十四届中轻万花杯 · 金奖",
        "award_en": "14th Zhongqing Wanhua Cup · Gold Award",
    },
    {
        "slug": "sishi-eryu",
        "category": "石雕创作",
        "category_en": "Stone Sculpture",
        "num": "N°SC-2013-001",
        "title": "似是而非的艺术",
        "title_en": "Art of Ambiguity",
        "year": "2013",
        "location": "",
        "location_en": "",
        "material": "宝兴大理石",
        "material_en": "Baoxing Marble",
        "dimensions": "可变尺寸",
        "dimensions_en": "Variable Dimensions",
        "hero_img": "../images/shishi-eryu.webp",
        "gallery": ["../images/shishi-eryu.webp"],
        "intro": "2013年毕业创作，对材料本质的初次探索。以宝兴大理石为媒介，在似是而非的形态中探寻雕塑与材料、具象与抽象的边界。这件作品奠定了老赵此后'从材料出发'的创作方法论。",
        "intro_en": "Graduation work, 2013 — an initial exploration of material essence. Using Baoxing marble as the medium, it probes the boundaries between sculpture and material, figuration and abstraction, in a form that is neither one nor the other. This work laid the foundation for Zhao's 'material-first' creative methodology.",
        "story": "这是老赵在川美雕塑系的毕业创作。当时导师问他：你雕的是什么？他说：你看到什么就是什么。导师笑了笑说：这就对了。从那时起，老赵就确定了自己的方向——雕塑不是告诉别人这是什么，而是让别人自己去感受这是什么。",
        "story_en": "Zhao's graduation work at Sichuan Fine Arts Institute. His advisor asked: 'What are you carving?' He replied: 'Whatever you see it as.' The advisor smiled: 'Now you've got it.' From that moment, Zhao knew his direction — sculpture isn't about telling people what it is, but letting them feel what it is.",
    },
    {
        "slug": "duihua",
        "category": "石雕创作",
        "category_en": "Stone Sculpture",
        "num": "N°SC-2021-002",
        "title": "对话",
        "title_en": "Dialogue",
        "year": "2021",
        "location": "",
        "location_en": "",
        "material": "陨石 · 鹅卵石 · 香樟木 · 镀锌管",
        "material_en": "Meteorite · Pebble · Camphor Wood · Galvanized Pipe",
        "dimensions": "可变尺寸",
        "dimensions_en": "Variable Dimensions",
        "hero_img": "../images/duihua.webp",
        "gallery": ["../images/duihua.webp"],
        "intro": "陨石来自宇宙深处，鹅卵石来自地球河流，香樟木来自人类庭院——三种完全不同的物质在镀锌管的工业语言中进行对话。每一种材料都在讲述自己的时间故事：亿万年、千万年、数十年，在雕塑中相遇。",
        "intro_en": "A meteorite from deep space, a pebble from an earthly river, camphor wood from a human courtyard — three radically different substances in dialogue through the industrial language of galvanized pipe. Each material tells its own temporal story: billions of years, millions of years, decades — meeting in sculpture.",
        "story": "陨石是朋友送的，鹅卵石是河边捡的，香樟木是拆迁老房子里拆下来的。三样东西放在一起，老赵盯了它们三天，然后开始做——不加修饰，不做变形，就是让它们各自立在镀锌管上。他说：'最好的对话不是我说服你、你说服我，而是我们各自站着，彼此听得见。'",
        "story_en": "The meteorite was a friend's gift, the pebble picked from a river, the camphor wood salvaged from a demolished old house. Zhao stared at the three objects for three days, then began — no embellishment, no distortion, just each standing on galvanized pipe. 'The best dialogue isn't about persuasion,' he said. 'It's about standing your ground, and still hearing each other.'",
    },
    {
        "slug": "baoxing-shanshui",
        "category": "石雕创作",
        "category_en": "Stone Sculpture",
        "num": "N°SC-2022-001",
        "title": "宝兴的山与水",
        "title_en": "Baoxing Mountain & Water",
        "year": "2022",
        "location": "",
        "location_en": "",
        "material": "宝兴大理石 · 树脂 · 不锈钢",
        "material_en": "Baoxing Marble · Resin · Stainless Steel",
        "dimensions": "可变尺寸",
        "dimensions_en": "Variable Dimensions",
        "hero_img": "../images/guanxin.webp",
        "gallery": [],
        "intro": "以宝兴本地大理石为主体，融入树脂和不锈钢，构建出山与水之间的诗意空间。大理石的自然纹理化为山峦的层叠，不锈钢的冷光如同水面的反射，树脂凝固了山水之间的雾气。",
        "intro_en": "Centered on local Baoxing marble with resin and stainless steel, constructing a poetic space between mountain and water. The marble's natural veining transforms into layered peaks, stainless steel's cold gleam mirrors water's surface, and resin captures the mist between them.",
        "story": "这件作品是老赵对宝兴这片土地的告白。在宝兴住了快十年，山和水早就刻进了眼睛里。他用本地大理石做山——因为山就是石头；用不锈钢做水——因为水会反光；用树脂封住中间——因为宝兴的雾，是山和水纠缠在一起的样子。",
        "story_en": "This work is Zhao's love letter to Baoxing. After nearly a decade there, the mountains and water are etched into his eyes. Local marble for the mountain — because mountains are stone. Stainless steel for water — because water reflects. Resin sealing the space between — because Baoxing's mist is mountain and water entangled.",
    },
    {
        "slug": "shanjian",
        "category": "石雕创作",
        "category_en": "Stone Sculpture",
        "num": "N°SC-2021-003",
        "title": "山涧",
        "title_en": "Mountain Stream",
        "year": "2021",
        "location": "",
        "location_en": "",
        "material": "宝兴大理石 · 锈铁",
        "material_en": "Baoxing Marble · Rusted Iron",
        "dimensions": "可变尺寸",
        "dimensions_en": "Variable Dimensions",
        "hero_img": "../images/shishi-eryu.webp",
        "gallery": [],
        "intro": "以宝兴大理石和锈铁两种材料构建，大理石的洁白与锈铁的暗红形成强烈对比。如同山间溪流切开裸露的岩层，时间在两种材质上留下完全不同的痕迹。",
        "intro_en": "Constructed from Baoxing marble and rusted iron — the marble's pure white contrasting starkly with the iron's dark rust. Like a mountain stream cutting through exposed strata, time leaves radically different marks on the two materials.",
        "story": "老赵说，山涧是最诚实的自然形态——水往低处流，石往深处裂，谁也不迁就谁。这件作品他只用了一天就确定了构图，但找了两个月才找到对的那块锈铁——锈得刚刚好，不多不少，就像山涧边的岩石被水汽浸了几百年。",
        "story_en": "Zhao says mountain streams are nature's most honest form — water flows downward, rock splits deeper, neither compromises. He settled the composition in one day, but spent two months finding the right piece of rusted iron — rusted just enough, neither too much nor too little, like a rock by a mountain stream weathered by centuries of mist.",
    },

    # ===== 制砚作品 =====
    {
        "slug": "shiershengxiao",
        "category": "制砚作品",
        "category_en": "Inkstone Art",
        "num": "N°IN-2025-001",
        "title": "十二生肖砚",
        "title_en": "Zodiac Inkstone Set",
        "year": "2025",
        "location": "四川雅安宝兴",
        "location_en": "Baoxing, Yaan, Sichuan",
        "material": "宝兴外朗石",
        "material_en": "Baoxing Wailang Stone",
        "dimensions": "十二方成套 · 每方约15×12cm",
        "dimensions_en": "Set of 12 · Each approx. 15×12cm",
        "hero_img": "../images/shiershengxiao.webp",
        "gallery": ["../images/shiershengxiao.webp"],
        "intro": "十二方成套穆坪砚，以中国传统十二生肖为主题，每方砚台对应一生肖，纯手工雕刻。外朗石质地温润细腻，发墨如油。每方品鉴皆呈现不同生肖的神韵与气质，成套收藏价值极高。",
        "intro_en": "A complete set of twelve Muping inkstones, each featuring one Chinese zodiac animal, all hand-carved. Wailang stone is fine and smooth, producing ink with an oil-like quality. Each stone captures the distinct spirit of its zodiac sign — a set of exceptional collectible value.",
        "story": "十二生肖砚是老赵耗时最长的一套砚台作品。从鼠到猪，每一方都要在石头上找到生肖的神韵——不是简单的动物浮雕，而是让石头本身的纹理参与到形象中去。比如龙砚，石头上天然有一道斜纹，恰似龙脊；比如兔砚，石材的温润感刚好契合兔的柔和。",
        "story_en": "The Zodiac Inkstones are Zhao's longest-running inkstone project. From Rat to Pig, each stone must capture the essence of its animal — not a simple relief, but letting the stone's natural veining participate in the image. The Dragon inkstone, for instance, has a natural diagonal vein exactly like a dragon's spine; the Rabbit inkstone's gentle stone texture perfectly matches the rabbit's softness.",
    },
    {
        "slug": "chuangwai",
        "category": "制砚作品",
        "category_en": "Inkstone Art",
        "num": "N°IN-2025-002",
        "title": "窗外",
        "title_en": "Outside the Window",
        "year": "2025",
        "location": "四川雅安宝兴",
        "location_en": "Baoxing, Yaan, Sichuan",
        "material": "宝兴外朗石",
        "material_en": "Baoxing Wailang Stone",
        "dimensions": "约18×12cm",
        "dimensions_en": "Approx. 18×12cm",
        "hero_img": "../images/chuangwai-1.webp",
        "gallery": ["../images/chuangwai-1.webp"],
        "intro": "以窗观心，砚中见天地。将传统砚台的实用功能与当代雕塑的空间概念相结合，砚池如窗，窗外是石纹天然形成的山水意境。一方小小的砚台，承载对自然的凝视与对内心的观照。",
        "intro_en": "Observing the heart through a window, seeing the world within an inkstone. Combining the inkstone's traditional function with contemporary sculptural spatial concepts — the ink pool is the window, beyond which the stone's natural veining forms a landscape. A small inkstone bearing the gaze upon nature and the reflection upon the self.",
        "story": "'窗外'这个意象来自老赵在宝兴工作室的日常——雕石头累了，抬头看看窗外的大山。他说砚池就是那扇窗，砚台周边的石皮是窗框，而砚心平整如镜的地方，倒映着天光和你的脸。一方砚，一扇窗，看的是山，见的是心。",
        "story_en": "'Outside the Window' was inspired by Zhao's daily routine at the Baoxing studio — looking up from stone carving to see the mountains through the window. The ink pool is that window, the surrounding stone skin is the frame, and the mirror-smooth ink-surface reflects the sky and your own face. One inkstone, one window — looking at mountains, seeing the heart.",
    },
    {
        "slug": "yuxi-lianye",
        "category": "制砚作品",
        "category_en": "Inkstone Art",
        "num": "N°IN-2025-003",
        "title": "鱼戏莲叶间",
        "title_en": "Fish Among Lotus Leaves",
        "year": "2025",
        "location": "四川雅安宝兴",
        "location_en": "Baoxing, Yaan, Sichuan",
        "material": "宝兴外朗石",
        "material_en": "Baoxing Wailang Stone",
        "dimensions": "系列多件 · 尺寸各异",
        "dimensions_en": "Series · Various Sizes",
        "hero_img": "../images/yuxi-lianye.webp",
        "gallery": ["../images/yuxi-lianye.webp"],
        "intro": "以汉乐府《江南》"鱼戏莲叶间"为灵感的外朗石砚系列。砚面上鱼与莲的线条在石纹中若隐若现，是水墨意境与石刻技艺的完美交融。浅浮雕鱼纹在墨汁浸润时仿佛游动起来。",
        "intro_en": "A Wailang stone inkstone series inspired by the Han-dynasty poem 'Fish Among Lotus Leaves'. Fish and lotus lines emerge and recede within the stone's veining — a perfect fusion of ink-wash aesthetics and stone-carving craft. The shallow-relief fish seem to swim when the ink pool is filled.",
        "story": "诗里写'鱼戏莲叶东，鱼戏莲叶西，鱼戏莲叶南，鱼戏莲叶北'——老赵觉得砚台也应该是这样：不同角度有不同的美。他刻意在砚台的四个方向做了不同深浅的浮雕，让使用者在研墨的时候，随着手腕转动能看到鱼在不同方位的莲叶间穿梭。",
        "story_en": "The poem goes: 'Fish play east of the lotus, fish play west of the lotus, fish play south of the lotus, fish play north of the lotus.' Zhao thought inkstones should be the same — beautiful from every angle. He deliberately carved reliefs of different depths on the four sides, so as you grind ink and turn your wrist, you see fish darting between lotus leaves in every direction.",
    },
    {
        "slug": "bajiaoyan",
        "category": "制砚作品",
        "category_en": "Inkstone Art",
        "num": "N°IN-2025-004",
        "title": "芭蕉砚系列",
        "title_en": "Plantain Inkstone Series",
        "year": "2025",
        "location": "四川雅安宝兴",
        "location_en": "Baoxing, Yaan, Sichuan",
        "material": "宝兴外朗石",
        "material_en": "Baoxing Wailang Stone",
        "dimensions": "系列三件 · 尺寸各异",
        "dimensions_en": "Series of 3 · Various Sizes",
        "hero_img": "../images/chuangwai-1.webp",
        "gallery": [],
        "intro": "以芭蕉叶为造型来源的外朗砚系列，三件作品各取芭蕉的不同形态：舒展、卷曲、残破。利用外朗石天然的黄绿交叠纹理，模拟蕉叶的色泽和质感，质朴天然中见匠心。",
        "intro_en": "A Wailang stone inkstone series based on plantain leaf forms — three works capturing different states: unfurling, curling, and worn. The stone's natural yellow-green layered veining simulates the plantain leaf's color and texture, revealing craftsmanship within natural simplicity.",
        "story": "老赵工作室门口种了一丛芭蕉。晴天雨天，叶子都好看。有一天他看着一片被虫咬出洞的芭蕉叶，突然觉得那个残缺比完整的叶子更有意思——就像砚台，完美的石头谁都能雕，但能在不完美的石头上做出有意思的东西，那才是本事。",
        "story_en": "A clump of plantain grows outside Zhao's studio. The leaves look beautiful rain or shine. One day, he noticed a leaf with holes eaten by insects, and suddenly found that imperfection more interesting than the pristine — just like inkstones. Anyone can carve a perfect stone, but making something compelling from the imperfect — that's true skill.",
    },
]


def make_page(work):
    """Generate a single work detail page."""
    loc_line = ""
    if work["location"]:
        loc_line = f'<div class="work-overline">{work["num"]} &nbsp;·&nbsp; {work["year"]} &nbsp;·&nbsp; {work["location"]}</div>'
    else:
        loc_line = f'<div class="work-overline">{work["num"]} &nbsp;·&nbsp; {work["year"]}</div>'

    gallery_html = ""
    if work["gallery"]:
        gallery_html = '<div class="work-gallery">\n'
        for img in work["gallery"]:
            gallery_html += f'            <img src="{img}" loading="lazy" alt="{work["title"]}">\n'
        gallery_html += '        </div>\n'

    award_html = ""
    if work.get("award"):
        award_html = f'''        <div class="work-spec-item">
            <div class="work-spec-label">获奖 Award</div>
            <div class="work-spec-value">{work["award"]}</div>
            <div class="work-spec-value en">{work["award_en"]}</div>
        </div>'''

    dims_html = ""
    if work.get("dimensions"):
        dims_html = f'''        <div class="work-spec-item">
            <div class="work-spec-label">尺寸 Dimensions</div>
            <div class="work-spec-value">{work["dimensions"]}</div>
            <div class="work-spec-value en">{work["dimensions_en"]}</div>
        </div>'''

    story_section = ""
    if work.get("story"):
        story_section = f'''    <div class="work-story">
        <div class="work-story-inner">
            <div class="tag">The Story</div>
            <h2>创作故事</h2>
            <blockquote>{work["story"]}</blockquote>
            <blockquote class="en">{work["story_en"]}</blockquote>
        </div>
    </div>'''

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{work["title"]} | 彦青雕塑 — {work["category"]}</title>
    <meta name="description" content="{work["title"]} — {work["category"]}作品。{work["material"]}。赵彦青创作。{work["year"]}年。">
    <meta property="og:title" content="{work["title"]} | 彦青雕塑">
    <meta property="og:description" content="{work["intro"][:150]}">
    <meta property="og:image" content="{BASE_URL}/{work["hero_img"]}">
    <link rel="canonical" href="{BASE_URL}/works/{work["slug"]}.html">
    <link rel="icon" type="image/png" href="../logo.png">
    <meta name="theme-color" content="#0a0a0a">
    <meta name="robots" content="index, follow">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "VisualArtwork",
        "name": "{work["title"]}",
        "creator": {{"@type": "Person", "name": "赵彦青"}},
        "artMedium": "{work["material"]}",
        "dateCreated": "{work["year"]}"{"","locationCreated": "" + work["location"] + """ if work["location"] else ""}
    }}
    </script>
    <link rel="stylesheet" href="works.css">
</head>
<body>

<nav>
    <div class="nav-inner">
        <a href="../index.html" class="nav-brand-wrap">
            <img src="../logo.png" alt="彦青雕塑" class="nav-logo">
            <span class="nav-brand">MAISON <span>·</span> YANQING</span>
        </a>
        <ul class="nav-links">
            <li><a href="../index.html#about">关于</a></li>
            <li><a href="../index.html#portfolio">作品</a></li>
            <li><a href="../index.html#projects">项目</a></li>
            <li><a href="../index.html#honors">荣誉</a></li>
            <li><a href="../index.html#contact">联系</a></li>
        </ul>
        <div class="breadcrumb">
            <a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="index.html">Works</a> &nbsp;/&nbsp; <span>{work["category"]}</span>
        </div>
    </div>
</nav>

<div class="work-container">
    <div class="work-header">
        {loc_line}
        <h1 class="work-title">{work["title"]}</h1>
        <p class="work-subtitle">{work["title_en"]}</p>
        <div class="work-line"></div>
    </div>

    <img src="{work["hero_img"]}" alt="{work["title"]}" class="work-hero" loading="lazy">

    <div class="work-grid">
        <div class="work-col">
            <div class="work-col-label">Details</div>
            <h2>作品信息</h2>
            <div class="work-specs">
                <div class="work-spec-item">
                    <div class="work-spec-label">类别 Category</div>
                    <div class="work-spec-value">{work["category"]}</div>
                    <div class="work-spec-value en">{work["category_en"]}</div>
                </div>
                <div class="work-spec-item">
                    <div class="work-spec-label">年份 Year</div>
                    <div class="work-spec-value">{work["year"]}</div>
                </div>
                <div class="work-spec-item">
                    <div class="work-spec-label">材料 Material</div>
                    <div class="work-spec-value">{work["material"]}</div>
                    <div class="work-spec-value en">{work["material_en"]}</div>
                </div>
                {dims_html}
                {award_html}
            </div>
            {"<p>" + work["intro"] + "</p>" if work["intro"] else ""}
            <p class="en">{"".join(work["intro_en"]) if work["intro_en"] else ""}</p>
        </div>
        <div class="work-col">
            <div class="work-col-label">Atelier Notes</div>
            <h2>收藏证书信息</h2>
            <div class="work-cert">
                <div class="work-cert-title">Certificate of Authenticity</div>
                <h3>{work["num"]}</h3>
                <p>{work["title"]}<br>赵彦青 创作 · 纯手工孤品</p>
                <p class="en">{work["title_en"]}<br>Handcrafted by Zhao Yanqing · Unique Piece</p>
                <p class="en" style="margin-top:1rem;">Materials: {work["material_en"]}<br>Year: {work["year"]}{" · Location: " + work["location"] if work["location"] else ""}</p>
                <div class="atelier">MAISON <span>·</span> YANQING <span>·</span> ATELIER <span>·</span> Est. MMXVI</div>
            </div>
        </div>
    </div>

    {gallery_html}
    {story_section}

    <div class="work-back">
        <a href="index.html">← 返回作品目录 / Back to Works</a>
    </div>
</div>

<footer>
    <div class="footer-brand">MAISON <span>·</span> YANQING <span>·</span> ATELIER</div>
    <div class="footer-tagline">Est. MMXVI · Chongqing &amp; Baoxing</div>
    <div class="footer-copy">&copy; 2016–2026 重庆彦青雕塑艺术有限公司 · 宝兴彦青雕塑艺术有限公司</div>
</footer>

</body>
</html>'''


if __name__ == "__main__":
    os.makedirs(WORKS_DIR, exist_ok=True)
    count = 0
    for w in works:
        path = os.path.join(WORKS_DIR, f'{w["slug"]}.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(make_page(w))
        print(f"  OK: {path}")
        count += 1
    print(f"\nGenerated {count} work detail pages.")
