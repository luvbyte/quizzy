<template>
  <div @click.self="close" class="fixed z-60 inset-0 fscreen">
    <div class="w-[80%] h-full flex flex-col p-2 bg-base-100 shadow-xl">
      <pre
        class="text-[0.6rem] font-bold flex flex-col p-4 flex justify-center items-center"
      >
   ___     _   _             _____   _____   __   __ 
  / " \ U |"|u| |   ___     |"_  /u |"_  /u  \ \ / / 
 | |"| | \| |\| |  |_"_|    U / //  U / //    \ V /  
/| |_| |\ | |_| |   | |     \/ /_   \/ /_    U_|"|_u 
U \__\_\u<<\___/  U/| |\u   /____|  /____|     |_|   
   \\// (__) )(.-,_|___|_,-._//<<,- _//<<,-.-,//|(_  
  (_(__)    (__)\_)-' '-(_/(__) (_/(__) (_/ \_) (__) </pre
      >

      <h1 class="text-center opacity-60 text-xs">Version - {{ VERSION }}</h1>

      <!-- themes -->
      <div class="flex flex-col overflow-hidden text-xs">
        <h1 class="divider m-0 uppercase">Theme ☷ {{ currentTheme }}</h1>
        <div
          class="rounded py-1 grid grid-rows-1 grid-flow-col space-x-1 overflow-x-auto scrollbar-hide"
        >
          <div
            v-for="theme in themes"
            :data-theme="theme"
            @click="setTheme(theme)"
            class="w-12 h-12 border-2 shrink-0 rounded-full flex items-center justify-center gap-1 p-1 active:border-base-content"
            :class="
              currentTheme === theme
                ? 'border-base-content'
                : 'border-base-content/20'
            "
          >
            <div class="w-1 h-4 bg-primary rounded"></div>
            <div class="w-1 h-4 bg-secondary rounded"></div>
            <div class="w-1 h-4 bg-info rounded"></div>
            <div class="w-1 h-4 bg-primary rounded"></div>
          </div>
        </div>
        <div class="divider m-0"></div>
      </div>

      <div class="flex-1">
        <!-- Social -->
        <div class="flex flex-col rounded-lg p-2">
          <h1 class="text-base-content/60 mb-3">SOCIAL</h1>

          <a
            href="https://instagram.com/4b_49_4b_4b_55"
            target="_blank"
            class="flex justify-between items-center no-underline"
          >
            <div>Instagram</div>
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
              >
                <g fill="none" stroke="currentColor" stroke-width="1.5">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M12 16a4 4 0 1 0 0-8a4 4 0 0 0 0 8"
                  />
                  <path
                    d="M3 16V8a5 5 0 0 1 5-5h8a5 5 0 0 1 5 5v8a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5Z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="m17.5 6.51l.01-.011"
                  />
                </g>
              </svg>
            </div>
          </a>
          <div class="divider m-0"></div>
          <a
            href="https://github.com/luvbyte"
            target="_blank"
            class="flex justify-between items-center no-underline"
          >
            <div>Github</div>
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5c.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34c-.46-1.16-1.11-1.47-1.11-1.47c-.91-.62.07-.6.07-.6c1 .07 1.53 1.03 1.53 1.03c.87 1.52 2.34 1.07 2.91.83c.09-.65.35-1.09.63-1.34c-2.22-.25-4.55-1.11-4.55-4.92c0-1.11.38-2 1.03-2.71c-.1-.25-.45-1.29.1-2.64c0 0 .84-.27 2.75 1.02c.79-.22 1.65-.33 2.5-.33s1.71.11 2.5.33c1.91-1.29 2.75-1.02 2.75-1.02c.55 1.35.2 2.39.1 2.64c.65.71 1.03 1.6 1.03 2.71c0 3.82-2.34 4.66-4.57 4.91c.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2"
                />
              </svg>
            </div>
          </a>
          <div class="divider m-0"></div>
          <a
            href="https://kikku.vercel.app"
            target="_blank"
            class="flex justify-between items-center no-underline"
          >
            <div>Portfolio</div>
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 48 48"
              >
                <g fill="none" stroke="currentColor" stroke-width="3">
                  <path
                    stroke-linejoin="round"
                    d="M3.539 39.743c.208 2.555 2.163 4.51 4.718 4.718C11.485 44.723 16.636 45 24 45s12.515-.277 15.743-.539c2.555-.208 4.51-2.163 4.718-4.718C44.723 36.515 45 31.364 45 24s-.277-12.515-.539-15.743c-.208-2.555-2.163-4.51-4.718-4.718C36.515 3.277 31.364 3 24 3s-12.515.277-15.743.539c-2.555.208-4.51 2.163-4.718 4.718C3.277 11.485 3 16.636 3 24s.277 12.515.539 15.743Z"
                  />
                  <path stroke-linecap="round" d="M3.5 13.5h41" />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M10 8.5h2m6 0h2"
                  />
                </g>
              </svg>
            </div>
          </a>
        </div>
        <!-- Support -->
        <div class="flex flex-col rounded-lg p-2">
          <h1 class="text-base-content/60 mb-3">SUPPORT</h1>
          <a
            href="/terms.html"
            target="_blank"
            class="flex justify-between items-center no-underline"
          >
            <div>Terms of use</div>
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M4 4a2 2 0 0 1 2-2h8a1 1 0 0 1 .707.293l5 5A1 1 0 0 1 20 8v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm13.586 4L14 4.414V8zM12 4H6v16h12V10h-5a1 1 0 0 1-1-1zm-4 9a1 1 0 0 1 1-1h6a1 1 0 1 1 0 2H9a1 1 0 0 1-1-1m0 4a1 1 0 0 1 1-1h6a1 1 0 1 1 0 2H9a1 1 0 0 1-1-1"
                />
              </svg>
            </div>
          </a>
          <div class="divider m-0"></div>
          <a
            href="/privacy.html"
            target="_blank"
            class="flex justify-between items-center no-underline"
          >
            <div>Privacy policy</div>
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M12 17a2 2 0 0 1-2-2c0-1.11.89-2 2-2a2 2 0 0 1 2 2a2 2 0 0 1-2 2m6 3V10H6v10zm0-12a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V10c0-1.11.89-2 2-2h1V6a5 5 0 0 1 5-5a5 5 0 0 1 5 5v2zm-6-5a3 3 0 0 0-3 3v2h6V6a3 3 0 0 0-3-3"
                />
              </svg>
            </div>
          </a>
          <div class="divider m-0"></div>
          <a
            href="mailto:lovemelong@protonmail.com"
            class="flex justify-between items-center no-underline"
          >
            <div>Contact</div>
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M4 20q-.825 0-1.412-.587T2 18V6q0-.825.588-1.412T4 4h16q.825 0 1.413.588T22 6v12q0 .825-.587 1.413T20 20zm8-7L4 8v10h16V8zm0-2l8-5H4zM4 8V6v12z"
                />
              </svg>
            </div>
          </a>
        </div>
      </div>

      <!-- footer -->
      <pre class="flex justify-center items-center text-xs">
        
♡  ∩_∩
 （„• ֊ •„)♡
┏ • UU • - • - • - • - • - • - • ღ❦ღ┓</pre
      >
      <div class="text-sm flex items-center gap-1 justify-center my-4">
        <span class="badge badge-sm badge-primary font-semibold font-heading"
          >Quizzy</span
        >
        ツ
        <span class="badge badge-sm badge-secondary font-semibold font-heading"
          >kikku ᥫ᭡</span
        >
      </div>
      <pre class="flex justify-center items-center text-xs">
┗ღ❦ღ • - • - • - • - • - • -- •- •  ┛
      </pre>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, onBeforeMount } from "vue";
  import { getTheme, applyTheme, VERSION } from "@/api/config";

  defineProps(["close"]);

  // Daisyui themes
  const themes = [
    "valentine",
    "dracula",
    "light",
    "caramellatte",
    "dim",
    "retro",
    "black",
    "cupcake",
    "bumblebee",
    "emerald",
    "corporate",
    "synthwave",
    "dark",
    "halloween",
    "garden",
    "forest",
    "lofi",
    "pastel",
    "fantasy",
    "wireframe",
    "luxury",
    "cmyk",
    "autumn",
    "business",
    "acid",
    "lemonade",
    "night",
    "coffee",
    "winter",
    "nord",
    "sunset",
    "abyss",
    "silk"
  ];

  const currentTheme = ref(getTheme());

  function setTheme(name) {
    applyTheme(name);
    currentTheme.value = name;
  }

  onMounted(async () => {
    applyTheme(currentTheme.value);
  });
</script>
