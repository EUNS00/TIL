<template>
  <div>
    <h1>여기는 최상위 컴포넌트</h1>
    <TodoList category="잠온다"></TodoList>
    <TodoList category="잠자자"></TodoList>
    <TodoList category="쳐자자"></TodoList>
  </div>
  
</template>

<script>
import TodoList from './components/TodoList.vue'

export default {
  components: {
    TodoList,
  }
}
</script>

<style>
</style>