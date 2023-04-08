# 反debugger

## 构造器debugger

```js
// 先保留原来的构造器函数
Function.prototype.constructor_ = Function.prototype.constructor;

Function.prototype.constructor = function(a){ 
    if(a=="debugger"){
        return function(){}
    }
    return Function.prototype.constructor_
}
```

# hook变量生成位置

## 猿人学第一题定位window全局变量生成位置

```js
(function(){
    'use strict';
    Object.defineProperty(window, '\x66', {
        set:function(x){console.log(x);debugger; return x;}
    })
})()

// Object.defineProperty() 方法会直接在一个对象上定义一个新的属性，或者修改一个对象的现有属性，并返回此对象
// set ：属性的setter函数，如果没有setter，则为undefine。当属性值被修改时，会调用此函数。该方法接受一个参数（也就是被赋予的新值），会传入赋值时的this对象。
```

## hook cookie生成位置

```js
(function(){
    'use strict';
    var cookieTemp = '';
    Object.defineProperty(window, 'cookie', {
        set:function(val){
            console.log("cookie设置位置：", val);
            debugger;
            cookieTemp = val;
            return cookieTemp;
        },
        get:function(){
            return cookieTemp;
        }
    }
})()
```



