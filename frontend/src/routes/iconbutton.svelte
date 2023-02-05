<script>
    export let name;
    export let src;
    export let alt;
</script>

<button on:click class="center">
    <div class=" border-solid border-2">
        {name} 
        <img src={src} alt={alt} class="w-16">
    </div>
</button>