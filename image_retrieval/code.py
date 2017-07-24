# coding: utf-8
import graphlab
image_train = graphlab.SFrame('image_train_data/')
image_train.head(5)
# 导入以前训练过的模型
deep_learning_model = graphlab.load_model('http://a3.amazonaws.com/GraphLab-Datasets/deeplearning/imagenet_model_iter45')
# 导入以前训练过的模型
deep_learning_model = graphlab.load_model('http://s3.amazonaws.com/GraphLab-Datasets/deeplearning/imagenet_model_iter45')
image_train.show()
knn_model = graphlab.nearest_neighbors.create(image_train, features=[image_train['deep_features'], label='id')
knn_model = graphlab.nearest_neighbors.create(image_train, features=image_train['deep_features'], label='id')
knn_model = graphlab.nearest_neighbors.create(image_train, features=['deep_features'], label='id')
cat = image_train[18:19]
cat
cat['image'].show()
knn_model.query(cat)
# 通过id过滤结果，取出图片
def get_images_from_ids(query_result):
    return image_train.filter_by(query_result['reference_label'], 'id')
cat_neighbors = get_images_from_ids(knn_model.query(cat))
cat_neighbors
cat_neighbors['image'].show()
car = image_train[8:9]
car
car['image'].show()
get_images_from_ids(knn_model.query(car))
get_images_from_ids(knn_model.query(car))['image'].show()
show_neighbors = lambda i: get_images_from_ids(knn_model.query(i))['image'].show()
show_neighbors(car)
show_neighbors(cat)
show_neighbors = lambda i: get_images_from_ids(knn_model.query(image_train[i:i+1]))['image'].show()
show_neighbors(1)
show_neighbors(99)
show_neighbors(9)
