import boto3

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

def list_buckets():
    for bucket in s3.buckets.all():
        print(bucket.name)

def get_bucket_by_name(bucket_name):
    bucket = s3.Bucket(bucket_name)

    if bucket.creation_date:
        return True
    else:
        print("Bucket não exite ome")

def create_object(bucket_name):
    obj = open('eu.PNG', 'rb')
    s3.Bucket(bucket_name).put_object(Key='eu.PNG', Body=obj)
    print('Objeto criado com sucesso!')

def delete_object(bucket_name):
    s3_client.delete_object(Bucket=bucket_name, Key='eu.PNG')
    print('Objeto deletado com sucesso!')

def init():
    print('*************************')
    print("1- Busca Buckets")
    print("2- Grava Eu no Bucket")
    print("3- Deleta Eu do Bucket")

    action = input('Digite qual função você que executar: ')

    if action == '1':
        list_buckets()
    elif action == '2':
        bucket_name = input("Digite o nome do bucket: ")
        exists = get_bucket_by_name(bucket_name)

        if exists:
            create_object(bucket_name)
    elif action == '3':
        bucket_name = input("Digite o nome do bucket: ")
        exists = get_bucket_by_name(bucket_name)

        if exists:
            delete_object(bucket_name)
    else:
        print("Bah crock omi do ceu omi")

if (__name__ == "__main__"):
    init()
