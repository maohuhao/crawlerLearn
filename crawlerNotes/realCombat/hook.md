# hook debugger

## eval hook
```js
var eval_ = eval;
function eval(a){
	if(a.contains("debugger")){
		eval("")
	}else{
		eval(a)
	}
}
```
## setInterval定时器hook
```js
// 针对定时器的回调函数中存在bugger字符，根据具体情况改写
var setInterval_ = setInterval
setInterval = function (func, time){
	console.log(func.toString());
	if(func.toString().includes('bugger')) {
		return function () {}; 
	} 
	return setInterval_(func, time)
}
```
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
猿人学第一题定位window全局变量生成位置

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
(function() {
    //严谨模式 检查所有错误
    'use strict';
    //document 为要hook的对象   这里是hook的cookie
	var cookieTemp = "";
    Object.defineProperty(document, 'cookie', {
		//hook set方法也就是赋值的方法 
		set: function(val) {
				//这样就可以快速给下面这个代码行下断点
				//从而快速定位设置cookie的代码
            	debugger;
				console.log('Hook捕获到cookie设置->', val);
				cookieTemp = val;
				return val;
		},
		//hook get方法也就是取值的方法 
		get: function()
		{
			return cookieTemp;
		}
    });
})();
```

# webpack hook

```js
window.token = d;
window._wbpk = a.toString()+":"+(e[a]+"")+",";
d = function(a){
	window._wbpk = window._wbpk + a.toString()+":"+(e[a]+"")+",";
	return window.token(a);
}
```