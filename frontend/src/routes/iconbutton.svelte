<script>
    export let name;
    export let src;
    export let alt;
    export let link="";
</script>

<a href={link} class="rounded-lg overflow-hidden border-solid border-2 shadow-lg p-2">
    <h4 class="text-center">{name}</h4>
    <img src={src} alt={alt} class="w-16">
</a>