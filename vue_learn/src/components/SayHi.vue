<template>
<div class="hi">
<!-- 静态数据测试 -->
hi,vue!
<br>
<!-- 动态数据测试 -->
{{message}}
<!-- 函数测试 -->
<input type="button" @click="show_my_value()" value="..." />
</div>
</template>

<script>

export default {
    data(){
        return{
            message : "你好，vue,这是一条动态信息",
            my_value : "from function show_my_value"
        }
    },
    methods : {
        show_my_value : function(){
            alert('my_value '+this.my_value);
            this.message = "change by <show_my_value>";
        }
    }
}
</script>

<style>
.hi{
    color: red;
    font-size: 20px;
}
</style>