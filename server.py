# -*- coding: utf-8 -*-
import codecs
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
# import DeviceFalutModels
import time
import json
import sys
import base64

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# import cv2
import numpy as np
import base64

# 服务端地址
host = ('localhost', 8000)

# ftp地址
#ftpPath = 'ftp://192.168.0.136:21/result/'

data = ''

class Resquest(BaseHTTPRequestHandler):
    # def handler(self):
    #     data = self.rfile.readline().decode()
    #     print("data:", self.rfile.readline().decode())
    #     self.wfile.write(self.rfile.readline())
    #
    # def do_GET(self):
    #     print(self.requestline)
    #     self.send_response(200)
    #     self.send_header('Content-type', 'application/json')
    #     self.end_headers()
    #     self.wfile.write(json.dumps(data).encode())

    # 接受post请求
    def do_POST(self):
        print('self.headers: %s' % self.headers)
        print('self.command: %s' % self.command)

        # 读取数据
        req_datas = self.rfile.read(int(self.headers['content-length']))
        req_datas_decode = req_datas.decode()
        print('req_datas.decode: %s' % req_datas_decode)

        req_datas_dic = json.loads(req_datas_decode)
        print('req_datas_dic: %s' % req_datas_dic)

        #保存图片
        imgFile = req_datas_dic['file']
        img = base64.b64decode(imgFile)
        print('img: %s' % img)
        with open('receivedPicure.jpg', 'wb') as f:
            f.write(img)

        req = json.loads(req_datas.decode())
        # print(req)
        # 检测
        result = Detection(req)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # 返回结果
        self.wfile.write(json.dumps(result).encode('utf-8'))


class ThreadingHttpServer(ThreadingMixIn, HTTPServer):
    pass


# 检测
def Detection(msg):
    return {}
    # img_decode_as = msg['file'].encode('ascii')
    # img_decode = base64.b64decode(img_decode_as)
    # img_np_ = np.frombuffer(img_decode, np.uint8)
    # img = cv2.imdecode(img_np_, cv2.COLOR_RGB2BGR)
    #
    # # 解析参数
    # labelList = msg['classes']
    # threshold = msg['vis_thresh']
    # print(labelList, threshold)
    #
    # if threshold < 0.1:
    #     threshold = 0.1
    #
    # imgName = 'abc.jpg'#get_current_time() + '.jpg'
    # imgPath = './recvPics/' + imgName
    #
    # # 判断图片是否有效
    # try:
    #     cv2.imwrite(imgPath, img)
    # except:
    #     print('img broken!')
    #     return {"code": "503", "result": 'null', 'msg': '未处理的异常'}
    # else:
    #     print('recvpic path: ', imgPath)
    #
    # common_res = DeviceFalutModels.run_infence(imgsname= [imgPath], threshold, contestantId="1")
    # # for test
    # common_res = [['wcgz', 0.61, [984, 38, 1454, 551]], ['wcaqm', 0.51, [347, 12, 619, 326]],
    #               ['wcaqm', 0.57, [1148, 39, 1349, 288]]]
    # # common_res = []
    # print(common_res)
    #
    # if len(common_res) == 0:
    #     print("recognized nothing")
    #
    # result = []
    # id = 0
    # # 在所有结果中查找指定标签
    # for i in range(len(common_res)):
    #     for j in range(len(labelList)):
    #         res = {}
    #         if common_res[i][0] == labelList[j]:
    #             id = id + 1
    #             res['id'] = id
    #             res['label'] = labelList[j]
    #             res['type'] = parseFaultType(labelList[j])
    #             res['scores'] = float(common_res[i][1])
    #             if labelList[j] == 'kgg_ybh' or labelList[j] == 'kgg_ybf':
    #                 res['isAlarm'] = 0
    #             else:
    #                 res['isAlarm'] = 1
    #
    #             res['bbox'] = common_res[i][2]
    #             result.append(res)
    #
    #             # print(result)
    #
    # # 保存在本地的图片文件名称
    # strImgFile = imgName
    # print(strImgFile)
    #
    # RetData = {}
    # if len(result) == 0:
    #     RetData["code"] = 210
    #     RetData["result"] = 'null'
    #     RetData["msg"] = '未识别到缺陷'
    #
    # else:
    #     RetData["code"] = 200
    #     RetData["result"] = result
    #     # ftp路径
    #     RetData["img_url"] = ftpPath + imgName
    #     RetData["img_path"] = strImgFile
    #     RetData["msg"] = '识别成功'
    #
    # print('RetData: ', RetData)
    # return RetData


if __name__ == '__main__':
    myServer = ThreadingHttpServer(host, Resquest)

    print("Starting http server, listen at: %s:%s" % host)
    myServer.serve_forever()