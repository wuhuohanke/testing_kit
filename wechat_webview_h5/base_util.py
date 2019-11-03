# encoding=utf-8
import wechat_webview_h5.path_mapping as path
import time
import traceback
import config
import random
import wechat_webview_h5.log_handler as log_handler

logger = log_handler.logger


# 按xpath点击
def click_by_xpath(driver, xpath_key):
    try:
        print("[脚本]开始获取%s的位置" % xpath_key)

        key_element = driver.find_element_by_xpath(path.wx_xpath_dict[xpath_key])
        if key_element:
            print("[脚本]已找到%s元素位置。尝试点击" % xpath_key)
            logger.info("已找到%s元素位置。尝试点击" % xpath_key)
            key_element.click()
            time.sleep(2)
        else:
            print("[脚本]没有找到%s元素位置。无法点击" % xpath_key)
            logger.info("没有找到%s元素位置。无法点击" % xpath_key)
    except:
        print("[脚本]未定位到元素或未能点击，程序终止")
        logger.info("未定位到元素或未能点击，程序终止")
        driver.quit()


# 按classname点击（css selector）
def click_by_classname(driver, css_key):
    driver.find_element_by_css_selector(css_key).click()
    print("[脚本]已点击%s" % css_key)
    logger.info("已点击%s" % css_key)
    time.sleep(2)


# 按classname输入值（css selector）
def send_keys_by_classname(driver, css_key, input_content):
    driver.find_element_by_css_selector(css_key).send_keys(input_content)
    print("[脚本]已在%s填入%s" % (css_key, input_content))
    logger.info("已在%s填入%s" % (css_key, input_content))
    time.sleep(2)


# 按步骤进入微信指定菜单
def navigate_with_steps(driver, xpath_keys):
    try:
        for key in xpath_keys:
            click_by_xpath(driver, key)
            time.sleep(2)
    except:
        print("[脚本]未能跳转到指定位置，程序终止")
        logger.info("未能跳转到指定位置，程序终止")
        driver.quit()


# 切换至webview
def switch_to_webview(driver):
    contexts = driver.contexts
    if 'WEBVIEW_com.tencent.mm:tools' in contexts:
        print("[脚本]WEBVIEW在可切换范围内")
        logger.info("WEBVIEW在可切换范围内")
        driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
        time.sleep(2)
        if driver.current_context == "WEBVIEW_com.tencent.mm:tools":
            print("[脚本]context已切换至WEBVIEW_com.tencent.mm:tools")
            logger.info("context已切换至WEBVIEW_com.tencent.mm:tools")
        else:
            print("[脚本]WEBVIEW切换失败")
            logger.info("WEBVIEW切换失败")
            raise Exception
    else:
        print("[脚本]WEBVIEW不在可切换范围内")
        logger.info("WEBVIEW不在可切换范围内")
        raise Exception


# 切换至native
def switch_to_native(driver):
    contexts = driver.contexts
    if 'NATIVE_APP' in contexts:
        print("[脚本]NATIVE_APP在可切换范围内")
        logger.info("NATIVE_APP在可切换范围内")
        driver.switch_to.context("NATIVE_APP")
        time.sleep(2)
        if driver.current_context == "NATIVE_APP":
            print("[脚本]context已切换至NATIVE_APP")
            logger.info("context已切换至NATIVE_APP")
        else:
            print("[脚本]NATIVE_APP切换失败")
            logger.info("NATIVE_APP切换失败")
            raise Exception
    else:
        print("[脚本]NATIVE_APP不在可切换范围内")
        logger.info("NATIVE_APP不在可切换范围内")
        raise Exception


# 按指定类别判断元素是否存在。目前仅支持按classname定位
def element_exist_by(driver, bytype, name):
    by_flag = None
    try:
        if bytype == "byclass":
            driver.find_element_by_css_selector("." + name)
            print("[脚本]%s在当前页面存在" % name)
            logger.info("%s在当前页面存在" % name)
            by_flag = True
        elif bytype == "byresourceid":
            driver.find_element_by_xpath("//*[resource-id=\']" + name + "\']/")
            print("[脚本]%s在当前页面存在" % name)
            logger.info("%s在当前页面存在")
            by_flag = True
    except Exception as e:
        if bytype == "byclass":
            print("[脚本]%s在当前页面不存在" % name)
            logger.info("%s在当前页面不存在" % name)
        elif bytype == "byresourceid":
            print("[脚本]%s在当前页面不存在" % name)
            logger.info("%s在当前页面不存在" % name)
        by_flag = False
        traceback.print_exc(e)
    finally:
        return by_flag


# 返回指定属性是否存在
def get_element_exist_attr(driver, bytype, name, attrname):
    attr_value = ""
    try:
        if bytype == "byid":
            attr = driver.find_element_by_id(name).get_attribute(attrname)
            attr_value += attr
    except Exception as e:
        if bytype == "byid":
            print("[脚本]%s属性不存在" % attrname)
            logger.info("%s属性不存在" % attrname)
        traceback.print_exc(e)
    finally:
        return attr_value


# 获取链接上参数
def get_url_params():
    url_params = {}
    url = config.link_to_be_test
    if '?' in url:
        temp = (url.split('?')[1]).split('&')
        if len(temp) != 0:
            for i in temp:
                url_params[i.split('=')[0]] = i.split('=')[1]
    print("[脚本]当前链接中参数为%s" % url_params)
    logger.info("当前链接中参数为%s" % url_params)
    return url_params


# 获取cookie内something字段
def get_cookie_ck(driver):
    current_cookies = driver.get_cookies()
    current_cookie_ck = ""
    for i in current_cookies:
        if 'something' in str(i):
            current_cookie_ck += str(i['value'])
            print("[脚本]当前cookies中有something，值为%s" % current_cookie_ck)
            logger.info("当前cookies中有something，值为%s" % current_cookie_ck)
            break
    else:
        print("[脚本]当前cookies中没有something")
        logger.info("当前cookies中没有something")
    return current_cookie_ck


# 生成随机144手机号
def random_mobile():
    random_string = ""
    mobile = "144"
    for i in range(8):
        temp = random.randint(0, 9)
        random_string += str(temp)
    mobile += random_string
    print("[脚本]生成的随机手机号为%s" % mobile)
    logger.info("生成的随机手机号为%s" % mobile)
    return mobile


# 获取the key。重点是如何运行js代码
def get_the_key(driver):
    the_key = driver.execute_script("return window.moduleName.bridgeid.func('xxx')")
    if the_key is not None and not the_key:
        print("[脚本]已获得the_key, key值为%s" % the_key)
        logger.info("已获得the_key, key值为%s" % the_key)
    else:
        print("[脚本]无the_key")
        logger.info("无the_key")
    return the_key


# 清理当前页面cookie并刷新
def clear_cookie_and_refresh(driver):
    driver.delete_all_cookies()
    print("[脚本]已清除所有cookie")
    logger.info("已清除所有cookie")
    driver.refresh()
    time.sleep(10)
