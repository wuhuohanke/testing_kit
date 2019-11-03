# encoding=utf-8
import wechat_webview_h5.init_connection as init_connection
import time
import wechat_webview_h5.base_util as util
import wechat_webview_h5.config as config
import traceback
import wechat_webview_h5.log_handler as log_handler


def execute_script():
    try:
        # 进入微信
        """
            按步骤传入映射的key值
            1. 跳转至微信 - 我
            2. 进入收藏
            3. 找到收藏中指定文章并点击
            4. 在文章中点击链接，跳转到h5
        """
        util.navigate_with_steps(driver, ["mine", "favorite", "paragraph", "link"])
        time.sleep(2)

        # 进入H5，获取上下文
        contexts = driver.contexts
        print("[脚本]微信全部上下文：%s" % contexts)
        logger.info("微信全部上下文：%s" % contexts)

        # 切换到webview
        util.switch_to_webview(driver)
        time.sleep(2)

        # 跳转至指定页面开始测试
        driver.execute_script("window.location.href=\'" + config.link_to_be_test + "\'")
        time.sleep(10)

        # 获取页面所有登录注册组件ID
        # 此处代码忽略        

        # 存储执行各脚本的结果
        scripts_result = []

        # 此处调用其他脚本获取结果，返回结果。代码忽略
        
        return scripts_result
    except Exception as e:
        logger.info(traceback.print_exc())
    finally:
        driver.quit()
        init_connection.kill_appium_server()


if __name__ == '__main__':

    # 引入logger实例
    logger = log_handler.logger

    # 确定期待结果配置没问题，以及确认是哪一种配置，再开始相应的跑脚本。此处代码忽略
    # 启动Appium server
    init_connection.start_appium_server()
    time.sleep(5)

    # 启动连接
    driver = init_connection.set_up()
    print("[脚本]初始化完成，启动微信")
    logger.info("初始化完成，启动微信")
    time.sleep(10)

    r = execute_script()
    print(r)
    logger.info("各脚本执行结果如下：%s" % str(r))
    