<script>
    export let name;
    export let src;
    export let alt;
    export let link="";
</script>

<a href={link} class="rounded-lg overflow-hidden border-solid border-2 shadow-lg p-2">
    <div class="center">
        {name} 
        <img src={src} alt={alt} class="w-16">
    </div>
</a>