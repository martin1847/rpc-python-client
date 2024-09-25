
import krpc

if __name__ == '__main__':
    channel=krpc.openChannel("idemo.wangyuedaojia.com")
    demo_svc=krpc.ServiceStub(channel
                ,app="demo-java-server",service="Demo"
                ,clientId="python-client-xxxxxxxxx"
                ,clientMeta='{"os":7}'
                ,accessToken=None)
    # print(demo_svc)
    # meta= [('cookie', 'a=b,c=d')]
    res = demo_svc.call("hello",{"name":"我是Python","age":28})
    if res.code ==0 :
        import json
        print('{"code":0,"data":',json.dumps(res.data),'}')
        # print(res.toJson())
    else:
        print("errror:",res.code,res.message)

