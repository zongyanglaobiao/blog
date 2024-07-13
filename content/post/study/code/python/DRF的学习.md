+++
title = 'DRF入门'
date = '{{ .Date }}'
description = "不用写SQL的Python Web框架"
+++
# Serializer

Django REST Framework (DRF) 提供了多种序列化器 (Serializer) 类，用于处理数据的序列化和反序列化。这些序列化器可以帮助你将复杂数据如查询集和模型实例转换为Python数据类型，这些数据类型然后可以很容易地被渲染成JSON、XML或其他内容类型。以下是DRF中一些主要的序列化器类型：

### 1. `Serializer`

基础的序列化器类，用于手动处理复杂的数据序列化。你需要定义每个字段，并可能需要手动实现创建和更新方法。它提供了最高的灵活性。

```Python
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    date_joined = serializers.DateTimeField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
```

### 2. `ModelSerializer`

继承自`Serializer`，自动根据模型生成序列化器字段，非常适合快速开发。它也自动实现了简单的创建和更新模型实例的方法。

```Python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyModel
        fields = '__all__'  #或者列出需要的字段 ['name', 'description']
```

### 3. `HyperlinkedModelSerializer`

与`ModelSerializer`类似，但它使用超链接来表示关联关系，而不是使用主键。

```Python
from rest_framework import serializers
from .models import MyModel

class MyHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = MyModel
        fields = ['url', 'name', 'owner']  'url' 是一个必要字段
        extra_kwargs = {
            'url': {'view_name': 'mymodel-detail'},
            'owner': {'view_name': 'user-detail'}
        }
```

### 4. `ListSerializer`

用于处理序列化对象列表的序列化器。通常，你不需要直接使用它，因为`ModelSerializer`和`Serializer`在定义字段时会自动处理列表字段。

### 5. `BaseSerializer`

所有其他序列化器的基类。通常不直接使用，但可以用于实现高度定制的序列化需求。

### 特殊字段和组件

除了这些基本序列化器类之外，DRF还提供了多种字段和组件，用于处理特定类型的数据：

- **字段类**：`CharField`, `IntegerField`, `DateField`, `DateTimeField`, `EmailField`, `FileField`, `ImageField`, `JSONField`, `ChoiceField`, `BooleanField` 等。
- **关联关系字段**：`PrimaryKeyRelatedField`, `HyperlinkedRelatedField`, `SlugRelatedField`, `StringRelatedField`。
- **验证和转换方法**：可以在序列化器中定义`validate_<fieldname>()`和`validate()`方法来进行数据验证。

这些序列化器和字段提供了丰富的功能，帮助你在Django项目中轻松地实现RESTful API的开发。

# `ModelSerializer`使用参考

`ModelSerializer` 是 Django REST Framework (DRF) 中的一个强大工具，用于自动将 Django 模型转换为序列化器。它基于模型字段自动生成相应的序列化器字段，并提供默认的实现来处理创建和更新模型实例的逻辑。使用 `ModelSerializer` 可以极大简化序列化器的代码量，特别是对于直接映射到数据库模型的简单 API。

### ModelSerializer 基础使用

先看一个基础示例，其中定义了一个用于操作 `Post` 模型的 `ModelSerializer`：

```Python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  包括模型中的所有字段
```

在这个基本的 `ModelSerializer` 中，`Meta` 类定义了序列化器将操作的模型 (`model`) 和包括哪些字段 (`fields`)。`fields = '__all__'` 表示包含模型中定义的所有字段。

### 自定义逻辑的入口

#### 字段级自定义

你可以在序列化器中声明额外的字段或者重写现有字段的行为：

```Python
class PostSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(default=True)  
    #添加额外的字段
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)  #将 'author' 字段设置为只读
    def validate_title(self, value):
        """ 自定义标题字段的验证逻辑 """
        if 'Django' not in value:
            raise serializers.ValidationError("Title must include the word 'Django'")
        return value
```

#### 实例创建和更新的自定义

`ModelSerializer` 提供了 `create()` 和 `update()` 方法，你可以重写这些方法以实现自定义的创建或更新逻辑：

```Python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    def create(self, validated_data):
        """ 自定义创建逻辑 """
        instance = Post.objects.create(**validated_data)
        #可以添加额外的处理逻辑
        return instance
    def update(self, instance, validated_data):
        """ 自定义更新逻辑 """
        instance.title = validated_data.get('title', instance.title)
        # 更新更多字段
        instance.save()
        return instance
```

#### 验证整体数据

除了字段级验证，你还可以重写 `validate()` 方法来添加整体数据的验证逻辑：

```Python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    def validate(self, data):
        """ 检查特定的条件是否满足 """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("end_date must occur after start_date")
        return data
```

#### 动态字段和条件逻辑

有时候，你可能希望基于请求或其他条件动态地调整序列化器的行为，如改变序列化的字段集：

```Python
class DynamicFieldsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'request' in self.context:
            if self.context['request'].user.is_anonymous:
                self.fields.pop('draft', None)
```

### 结论

`ModelSerializer` 提供了多种方式来自定义和扩展序列化器的功能。通过重写方法和自定义字段，你可以实现精确控制序列化和反序列化过程，从而满足不同的业务需求。使用 `ModelSerializer` 不仅可以减少重复代码，还能提高开发效率和维护性。

# View

Django REST Framework (DRF) 提供了多种视图组件，帮助开发者快速地构建 RESTful API。以下是DRF中一些主要的视图组件：

### 1. `APIView`

`APIView`是所有视图类的基类，提供了处理HTTP请求的基本方法。你可以通过重写`get()`, `post()`, `put()`, `delete()`等方法来处理不同类型的HTTP请求。

### 2. `GenericAPIView`

`GenericAPIView`继承自`APIView`，添加了对Django模型的支持，包括序列化器类、查询集等。这个视图本身不实现任何请求方法（如GET或POST），需要与`mixins`一起使用来添加这些方法。

1. Mixins

DRF提供了一系列mixin类，用于扩展`GenericAPIView`，以实现常见的API操作：

- `CreateModelMixin`：提供创建对象的方法。
- `ListModelMixin`：提供列出查询集的方法。
- `RetrieveModelMixin`：提供检索单个对象的方法。
- `UpdateModelMixin`：提供更新对象的方法。
- `DestroyModelMixin`：提供删除对象的方法。

### 4. `ListAPIView` 和 `CreateAPIView`

这些视图组合了`GenericAPIView`与相应的mixin，为常见的行为提供了现成的实现：

- `ListAPIView`：使用`ListModelMixin`，用于展示数据列表。
- `CreateAPIView`：使用`CreateModelMixin`，用于创建新的数据条目。

### 5. `RetrieveAPIView`, `UpdateAPIView`, `DestroyAPIView`

这些也是组合了`GenericAPIView`与相应的mixin：

- `RetrieveAPIView`：使用`RetrieveModelMixin`，用于获取单个数据详情。
- `UpdateAPIView`：使用`UpdateModelMixin`，用于更新数据。
- `DestroyAPIView`：使用`DestroyModelMixin`，用于删除数据。

### 6. `ListCreateAPIView`, `RetrieveUpdateAPIView`, `RetrieveDestroyAPIView`, `RetrieveUpdateDestroyAPIView`

这些视图组合了多个mixins，为更复杂的需求提供解决方案：

- `ListCreateAPIView`：结合列表显示和创建新对象的功能。
- `RetrieveUpdateAPIView`：结合检索和更新对象的功能。
- `RetrieveDestroyAPIView`：结合检索和删除对象的功能。
- `RetrieveUpdateDestroyAPIView`：结合检索、更新和删除对象的功能。

### 7. `ViewSet`

`ViewSet`类似于Django的`View`，但专为DRF设计，用于管理一组相关的请求处理操作。通常与路由器一起使用，以自动配置URL路由。

### 8. `ModelViewSet`

`ModelViewSet`自动提供`list`, `create`, `retrieve`, `update`, 和 `destroy`动作。它基本上结合了所有的mixin和`GenericAPIView`的功能。

### 使用实例

这些视图使得构建API变得非常快捷和高效。例如，如果你只需要一个API来列出所有对象和创建新对象，你可以使用`ListCreateAPIView`并简单地指定序列化器和查询集：

```Python
from rest_framework.generics import ListCreateAPIView
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreateAPIView(ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

这些视图和视图集极大简化了API的开发流程，使得开发者可以专注于业务逻辑而非基础架构代码

# `ModelViewSet`参考

`ModelViewSet` 在 Django REST Framework (DRF) 中是一个非常强大的工具，它结合了列表视图、创建视图、检索视图、更新视图和删除视图的功能。它提供了一系列方法和属性，使得你可以在单个类中处理与模型相关的所有 CRUD（创建、读取、更新、删除）操作。

### ModelViewSet 基础使用

先看一个简单的例子，其中定义了一个用于操作 `Post` 模型的 `ModelViewSet`：

```Python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

在这个基本的 `ModelViewSet` 中，`queryset` 属性定义了视图集将操作的模型对象集合，`serializer_class` 属性指定了用于序列化和反序列化数据的类。

### 自定义逻辑的入口

1. 动作方法

`ModelViewSet` 自动为你创建了 `list`, `create`, `retrieve`, `update`, `partial_update`, 和 `destroy` 这些动作。你可以通过重写这些方法来添加自定义逻辑：

```Python
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def list(self, request, *args, **kwargs):
        # 添加自定义逻辑
        response = super().list(request, *args, **kwargs)
        # 可以修改响应等
        return response
    def create(self, request, *args, **kwargs):
    # 自定义创建逻辑
        return super().create(request, *args, **kwargs)
    def retrieve(self, request, *args, **kwargs):
    # 自定义检索逻辑
        return super().retrieve(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
    # 自定义更新逻辑
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
    # 自定义删除逻辑
        return super().destroy(request, *args, **kwargs)
```

1. 查询集和序列化器的动态选择

在某些情况下，根据请求的不同，你可能需要使用不同的查询集或序列化器。你可以重写 `get_queryset` 和 `get_serializer_class` 方法来实现这一点：

```Python
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(active=True)
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializerel
        if self.action == 'retrieve':
            return PostDetailSerializer
        return DefaultPostSerializer
```

1. 验证和权限

你可以通过设置 `permission_classes` 和 `authentication_classes` 属性来控制访问权限和验证方式。此外，DRF 允许你在视图级别进行更细粒度的权限控制：

```Python
from rest_framework.permissions import IsAuthenticated, AllowAny

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_permissions(self):
        if self.action == 'retrieve':
            return [AllowAny()]
        return [IsAuthenticated()]
```

1. 过滤、排序和分页

DRF 支持强大的查询过滤、排序和分页功能。你可以通过设置 `filter_backends`, `filterset_class`, `ordering_fields`, `pagination_class` 等属性来配置这些功能：

```Python
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
```

### 结论

`ModelViewSet` 提供了非常灵活的方法来构建具有完整 CRUD 功能的 API。通过重写方法和配置属性，你可以轻松地定制视图的行为以满足具体需求。
