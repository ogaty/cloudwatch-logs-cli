# cloudWatchLogs from aws-cli

コンソール画面から見るの分かりづらいのでaws cliから見る

## ログストリーム一覧を取得
```
python3 list-events.py aws-profile logGroupName
```

### sample
```
tea@tina-1:~/cloudwatch$ python3 list-events.py default /aws/lambda/param 
2019-08-06 20:29:37 2019/08/06/[$LATEST]7899a1fc4c7e40fe85db5d8349c78e42
2019-08-06 20:27:34 2019/08/06/[$LATEST]508258af956c4ba89763aa21191bcb04
```

### この画面ね
![list](https://github.com/ogaty/my-documents/blob/master/cloudwatch/list.jpg)

## イベントの中身を取得
```
python3 get-event.py aws-profile logGroupName logStreamName
```

### sample
```
tea@tina-1:~/cloudwatch$ python3 get-event.py default /aws/lambda/param 2019/08/06/[\$LATEST]7899a1fc4c7e40fe85db5d8349c78e42
START RequestId: 0c81c25a-32a8-445b-ba4e-f531f2f90fdb Version: $LATEST


[ERROR] ClientError: An error occurred (AccessDeniedException) when calling the DescribeParameters operation: User: arn:aws:sts::268531527157:assumed-role/param-role-hbit0t7x/param is not authorized to perform: ssm:DescribeParameters on resource: arn:aws:ssm:ap-nort    raise error_class(parsed_response, operation_name) _make_api_call


END RequestId: 0c81c25a-32a8-445b-ba4e-f531f2f90fdb


REPORT RequestId: 0c81c25a-32a8-445b-ba4e-f531f2f90fdb	Duration: 1259.28 ms	Billed Duration: 1300 ms 	Memory Size: 128 MB	Max Memory Used: 74 MB	
```

### この画面ね
![get](https://github.com/ogaty/my-documents/blob/master/cloudwatch/get.jpg)


