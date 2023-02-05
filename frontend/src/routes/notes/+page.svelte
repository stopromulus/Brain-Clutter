<script>
    import { resize } from "$lib/resize.js";
    import { writable } from "svelte/store";

    let noteBoxes = [];

    function toRect({x, y, width, height}) {
        return [x, y, x + width, y + height];
    }
</script>

<div class="relative h-screen" on:click|self={(ev) => {
    let noteBox = {el: null, grab: null, content: '', width: 300, height: 100, x: ev.layerX - 150, y: ev.layerY - 50 };

    const [aX1, aY1, aX2, aY2] = toRect(noteBox);

    if (noteBoxes.filter(nb => {
        const [bX1, bY1, bX2, bY2] = toRect(nb);
        return aX2 >= bX1 && aX1 <= bX2 && aY1 <= bY2 && aY2 >= bY1;
    }).length) return;

    noteBoxes = [...noteBoxes, noteBox];
    setTimeout(() => {
        noteBox.el?.focus?.();
    });
}}>
    {#each noteBoxes as noteBox, idx}
        <div
            class="border-2 min-h-[2.8rem] border-gray-400 absolute rounded-lg overflow-hidden focus-within:resize focus-within:border-blue-500 p-2 bg-white"
            style="top:{noteBox.y}px; left:{noteBox.x}px; width:{noteBox.width}px; height:{noteBox.height}px;"
            use:resize={[writable(), el => {
                noteBox.width = el.offsetWidth;
                noteBox.height = el.offsetHeight;
            }]}
        >
            <textarea
                bind:this={noteBox.el}
                bind:value={noteBox.content}
                placeholder="Type here!"
                class="w-full h-full !outline-0 resize-none"
            ></textarea>
            <span on:click={() => {
                noteBoxes = noteBoxes.filter((_, i) => i !== idx);
            }} class="absolute text-xs top-[-2.5px] right-[0.3px] select-none cursor-pointer text-gray-600">X</span>
        </div>
    {/each}
</div>

