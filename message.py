#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#旋轉木馬按鈕訊息介面

#清 午晚
def Tsing_Dinner_Carousel():
    message = TemplateSendMessage(
        alt_text='口袋清單',#
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://miffycares.files.wordpress.com/2020/03/img_0437.jpg?w=1024', #首圖
                    title='The Loft',#主標
                    text='清夜推薦午/晚餐', #副標
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/EkJKUVqTRj6s7DZU7'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃The Lost',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.deliveryhero.io/image/fd-tw/LH/l6hk-hero.jpg?width=512&height=384&quality=45',
                    title='港島主麵',#done
                    text='清夜推薦午/晚餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/V2K6hcY6MRAykX659'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃港島主麵',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.deliveryhero.io/image/fd-tw/LH/a5rq-hero.jpg',
                    title='馬來老爹',#done
                    text='清夜推薦午/晚餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/CDvAU6wFisSTJCfb8'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃馬來老爹',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.deliveryhero.io/image/fd-tw/LH/r0oa-hero.jpg',
                    title='白鬍子',
                    text='清夜推薦午/晚餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/5qQS7q1pvJuYurus7'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text= '吃白鬍子',
                            data= 'r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                )
            ]
        )
    )
    return message


def Tsing_Drink_Carousel():
    message = TemplateSendMessage(
        alt_text='口袋清單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://images.deliveryhero.io/image/fd-tw/LH/k9h4-hero.jpg',
                    title='鶴茶樓',
                    text='清夜推薦飲料',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/NvKutJvWptRDAacU9'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='喝鶴茶樓',#DONE
                            data = 'r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.deliveryhero.io/image/fd-tw/LH/gfmk-hero.jpg',
                    title='五桐號',
                    text='清夜推薦飲料',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/Ue6HvaPWk3QTfPdx9'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='喝五桐號',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.deliveryhero.io/image/fd-tw/LH/u216-hero.jpg',
                    title='麻古',
                    text='清夜推薦飲料',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/Ko66n7kXodtEXRku5'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='喝麻古',
                            data='r'#DONE
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                )
            ]
        )
    )
    return message

def Tsing_Break_Carousel():
    message = TemplateSendMessage(
        alt_text='口袋清單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn( #Image已改
                    thumbnail_image_url='https://d1ralsognjng37.cloudfront.net/85de5bac-dbf2-4189-9979-5c77aaaed1ea.jpeg',
                    title='豬多好事',
                    text='清夜推薦早餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/bP1iB2dFAjXR2iXx8'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃豬多好事',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://d1ralsognjng37.cloudfront.net/caf5caae-2289-4562-bacf-673c14c00780.jpeg',
                    title='g day早餐店',#done
                    text='清夜推薦早餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/GkEWQMVhiLHPHT4U9'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃g day早餐店',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                )
            ]
        )
    )
    return message

def Tsing_Coffee_Carousel():
    message = TemplateSendMessage(
        alt_text='口袋清單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://sillybaby.tw/wp-content/uploads/DSC06080.jpg',
                    title='井井咖啡廳',
                    text='清夜推薦咖啡廳',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/fGaUfy5cFwT9rdks9'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃井井咖啡廳',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://static.popdaily.com.tw/u/202111/09a18c88-d847-4645-a408-dd68fb2599e3.jpg',
                    title='梁氏甜點',#done
                    text='清夜推薦咖啡廳',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/yvZPyHixUN3GM58W7'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃梁氏甜點',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.ltn.com.tw/Upload/playing/page/2014/07/05/140705-6059-1-KJg0K.jpg',
                    title='舊是經典',
                    text='清夜推薦咖啡廳',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/5kLu12bPN3FHTKfo7'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃舊是經典',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&清夜'
                        )
                    ]
                )
            ]
        )
    )
    return message



def City_Drink_Carousel():
    message = TemplateSendMessage(
        alt_text='口袋清單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://d1ralsognjng37.cloudfront.net/a62f4933-9d9f-48dc-81bd-9f7ae6507896.jpeg',
                    title='上宇林',
                    text='市區推薦飲料',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/oWEqcyyhPPQR4t9D9'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='喝上宇林',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://obs.line-scdn.net/0hkOnWf9g3NGBTLh7R9RtLN2l4Nw9gQidjNxhlYxBAalQsS3RmPE94DnAqYgB6GHM-PRh-D3YvL1EuHnBjbEx4/w644',
                    title='河堤上的貓',
                    text='市區推薦飲料',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/Cf5EdgkcijRerXQm7'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='喝河堤上的貓',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i1.achangpro.com/img.huablog.tw/uploads/20190910002929_39.jpg',
                    title='好哞',
                    text='市區推薦飲料',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/4Su6FeQVTVPvskYz7'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='喝好哞',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i1.achangpro.com/img.huablog.tw/uploads/20210123231158_69.jpg',
                    title='飽足感',
                    text='市區推薦飲料',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/MZcMVoJRMW7kmdfB6'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='喝飽足感',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                )
            ]
        )
    )
    return message

def City_Dinner_Carousel():
    message = TemplateSendMessage(
        alt_text='口袋清單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://ikuma.cc/wp-content/uploads/flickr/48207832932_7a2374d939_c.jpg',
                    title='太郎燒肉',
                    text='市區推薦午/晚餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/p5EsmYW3JmCwRihGA'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃太郎燒肉',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://ikuma.cc/wp-content/uploads/flickr/48207832932_7a2374d939_c.jpg',
                    title='麵屋浩',#done
                    text='市區推薦午/晚餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/LK9mw5ymd6QmrXPd9'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃麵屋浩',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://d1ralsognjng37.cloudfront.net/d6ab987b-907e-4796-8968-404cc0089af5.jpeg',
                    title='沐嵐',#done
                    text='市區推薦午/晚餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/Nfi94efy9uY6mpas8'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃沐嵐',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                )
            ]
        )
    )
    return message


def City_Coffee_Carousel():
    message = TemplateSendMessage(
        alt_text='口袋清單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t39.30808-6/282345245_1449666018801816_8515609034034339066_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_ohc=mlzKGntRgvAAX-kaUcG&_nc_oc=AQmp2BdGsh0pWLUpnCZWdTBnktJ8vCCFtwnL0Vj14TNw3o9tf9wLIAs9EZ2FiqlJ-hMiYppEy_oAyDAjg9m_7fIH&_nc_ht=scontent.ftpe8-2.fna&oh=00_AT_ZNDRgaB-Z7IjqO7ZjM9YPHK2dVViTNpawxpyXTZ3BCw&oe=62A20DAA',
                    title='暗室微光',
                    text='市區推薦咖啡廳',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/zLHF49AdS6x9cgM67'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃暗室微光',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://pic.pimg.tw/alice49717/1554038290-469374744_l.jpg',
                    title='階段甜點',#done
                    text='市區推薦咖啡廳',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/E4vkKzv6qrh3UfV8A'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃階段甜點',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://travelimg.yamedia.tw/20180811/20180810220919254.jpg',
                    title='墨咖啡',#done
                    text='市區推薦咖啡廳',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/Ta4XZAYPR4Wvwt6o8'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃墨咖啡',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                )
            ]
        )
    )
    return message


def City_Break_Carousel():
    message = TemplateSendMessage(
        alt_text='口袋清單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://static.wixstatic.com/media/116172_ae629119bab746e297415440da7eaa2c~mv2.jpg/v1/fit/w_712%2Ch_540%2Cal_c%2Cq_80/file.jpg',
                    title='默倪Morning Hsinchu 早午餐',
                    text='市區推薦早餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/XHbPribbLYvg7SrR7'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃默倪Morning Hsinchu 早午餐',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://d1ralsognjng37.cloudfront.net/6e80d958-7a3b-4521-b27d-e0cc8999a230.jpeg',
                    title='早安公雞',#done
                    text='市區推薦早餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/yNNenNUUsntbYxfG8'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃早安公雞'
                            ,
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://d1ralsognjng37.cloudfront.net/d5751afc-cc14-420f-a0ce-a6c84481ee10.jpeg',
                    title='阿婆早餐麵店',#done
                    text='市區推薦早餐',
                    actions=[
                        URITemplateAction(
                            label='開啟Google Map',
                            uri='https://goo.gl/maps/wiJHDz3gW7XQgftD7'
                        ),
                        PostbackTemplateAction(
                            label='就決定是你了！Pick',
                            text='吃阿婆早餐麵店',
                            data='r'
                        ),
                        PostbackTemplateAction(
                            label='Return',
                            text='Return',
                            data='L&市區'
                        )
                    ]
                )
            ]
        )
    )
    return message
#https://d1ralsognjng37.cloudfront.net/85de5bac-dbf2-4189-9979-5c77aaaed1ea.jpeg
