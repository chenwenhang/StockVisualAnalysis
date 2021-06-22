DB_USERNAME = 'root'
DB_PASSWORD = 'your password'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_DATABASE = 'stock'
DB_ENCODING = "utf8"
INDUSTRY_NUM_MAP = {
    "航空": 31,
    "特种钢": 10,
    "农用机械": 10,
    "纺织机械": 12,
    "批发业": 7,
    "轻工机械": 9,
    "仓储物流": 42,
    "商贸代理": 20,
    "专用机械": 168,
    "新型电力": 17,
    "汽车配件": 160,
    "普钢": 23,
    "其他商业": 13,
    "元器件": 226,
    "综合类": 34,
    "染料涂料": 24,
    "塑料": 58,
    "IT设备": 38,
    "化学制药": 121,
    "软件服务": 234,
    "船舶": 7,
    "火力发电": 28,
    "医疗保健": 116,
    "矿物制品": 23,
    "电气设备": 200,
    "机械基件": 88,
    "超市连锁": 12,
    "日用化工": 11,
    "林业": 4,
    "化工机械": 9,
    "纺织": 44,
    "钢加工": 26,
    "互联网": 71,
    "橡胶": 12,
    "中成药": 72,
    "酒店餐饮": 9,
    "生物制药": 60,
    "电器仪表": 78,
    "通信设备": 128,
    "供气供热": 32,
    "渔业": 7,
    "园区开发": 15,
    "环境保护": 112,
    "汽车服务": 10,
    "水力发电": 20,
    "造纸": 30,
    "机床制造": 15,
    "广告包装": 39,
    "化工原料": 198,
    "小金属": 37,
    "医药商业": 24,
    "半导体": 71,
    "农药化肥": 39,
    "房产服务": 12,
    "建筑工程": 89,
    "商品城": 2,
    "种植业": 16,
    "影视音像": 44,
    "软饮料": 9,
    "食品": 76,
    "服饰": 58,
    "装修装饰": 28,
    "摩托车": 9,
    "工程机械": 28,
    "区域地产": 51,
    "其他建材": 26,
    "证券": 47,
    "百货": 37,
    "运输设备": 31,
    "黄金": 12,
    "电器连锁": 1,
    "玻璃": 21,
    "多元金融": 26,
    "汽车整车": 22,
    "白酒": 20,
    "水务": 11,
    "保险": 9,
    "铜": 15,
    "公共交通": 9,
    "红黄酒": 10,
    "出版业": 21,
    "机场": 3,
    "文教休闲": 41,
    "全国地产": 28,
    "石油开采": 18,
    "陶瓷": 7,
    "化纤": 28,
    "港口": 15,
    "铝": 30,
    "铁路": 5,
    "银行": 35,
    "饲料": 16,
    "乳制品": 16,
    "家用电器": 48,
    "路桥": 21,
    "旅游景点": 11,
    "家居用品": 42,
    "铅锌": 12,
    "水运": 11,
    "电信运营": 9,
    "啤酒": 7,
    "焦炭加工": 8,
    "煤炭开采": 27,
    "空运": 8,
    "石油加工": 9,
    "旅游服务": 9,
    "公路": 2,
    "石油贸易": 7,
    "农业综合": 34,
    "水泥": 22,
}


class Settings(object):
    DEBUG = True
