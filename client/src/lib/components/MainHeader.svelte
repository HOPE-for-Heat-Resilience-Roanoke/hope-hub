<script>
  import { page } from '$app/stores';
</script>

<header
  class="fixed z-10 top-0 inset-x-0 border-b
    bg-white dark:bg-dark-background dark:border-gray-800"
>
  <nav
    class="flex items-center justify-between max-w-5xl
    mx-auto px-4 h-24"
  >
    <a href="/"> <img class="h-10 md:h-24" src="/images/logo.png" alt="HOPE for Heat Resilience Logo"/> </a>

    <div class="flex space-x-3 items-center">
      <a 
          class:font-bold={$page.url.pathname == "/"} href="/">home</a>
      <a 
          class:font-bold={$page.url.pathname == "/news"} href="/news">news</a>
      <a 
          class:font-bold={$page.url.pathname == "/about"} href="/about">about</a>
      <a 
          class="border-r border-black pr-3"
          class:font-bold={$page.url.pathname == "/people"} href="/people">people</a>
      <a 
          
          class:font-bold={$page.url.pathname == "/hub"} href="/hub">Digital Hub</a>
    </div>

  </nav>
</header>
