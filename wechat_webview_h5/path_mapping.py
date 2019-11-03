# encoding=utf-8
# 微信中进入H5的操作。dict中按顺序存放
# mine：微信-我
# favorite：微信-收藏
# paragraph：收藏中的第一篇文章
# link：进入文章后要点击的h5链接（提前收藏好）

wx_xpath_dict = {
    "mine": "//*[@resource-id=\'com.tencent.mm:id/bq\']"
                                    "/child::android.widget.LinearLayout"
                                    "/child::android.widget.RelativeLayout[4]",
    "favorite": "//*[@resource-id=\'android:id/list\']"
                                    "/child::android.widget.LinearLayout[2]",
    "paragraph": "//*[@resource-id=\'com.tencent.mm:id/bv6\']"
                                    "/child::android.widget.FrameLayout[1]",
    "link": "//*[@resource-id=\'com.tencent.mm:id/bvj\']"
}
