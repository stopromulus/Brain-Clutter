<script>
    import {resize} from "$lib/resize.js";
    import {writable} from "svelte/store";
    import {PUBLIC_API_URL} from "$env/static/public";

    export let data;
    let {notes: noteBoxes} = data;

    function toRect({x, y, width, height}) {
        return [x, y, x + width, y + height];
    }

    function addNoteBox(ev) {
        let noteBox = {
            id: null,
            el: null,
            grab: null,
            content: '',
            width: 300,
            height: 100,
            x: ev.pageX - 150,
            y: ev.pageY - 50
        };

        const [aX1, aY1, aX2, aY2] = toRect(noteBox);

        if (noteBoxes.filter(nb => {
            const [bX1, bY1, bX2, bY2] = toRect(nb);
            return aX2 >= bX1 && aX1 <= bX2 && aY1 <= bY2 && aY2 >= bY1;
        }).length) return;

        fetch(`${PUBLIC_API_URL}/notes/`, {
            method: 'POST',
            body: JSON.stringify({
                content: noteBox.content, width: noteBox.width, height: noteBox.height, x: noteBox.x, y: noteBox.y
            }),
            headers: {
                'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
        }).then(res => res.json()).then(res => {
            console.log(res);
            noteBox.id = res.id;
            noteBoxes = [...noteBoxes, noteBox];
            setTimeout(() => {
                noteBox.el?.focus?.();
            });
        })
    }

    async function saveNoteBox(noteBox) {
        await fetch(`${PUBLIC_API_URL}/notes/${noteBox.id}/`, {
            method: 'PUT',
            body: JSON.stringify({
                content: noteBox.content, width: noteBox.width, height: noteBox.height, x: noteBox.x, y: noteBox.y
            }),
            headers: {
              'Content-Type': 'application/json',
            },
        })
    }

    function debounce(func, timeout = 300){
        let timer;
        return (...args) => {
            clearTimeout(timer);
            timer = setTimeout(() => { func.apply(this, args); }, timeout);
        };
    }

    const debouncedSave = debounce(saveNoteBox, 300);
</script>

<div class="relative h-screen" on:click|self={addNoteBox}>
    {#if noteBoxes.length === 0}
        <p on:click={addNoteBox} class="text-3xl text-gray-400 text-center pt-[40vh] select-none">
            Click/tap anywhere to make a note!
        </p>
    {/if}
    {#each noteBoxes as noteBox, idx}
        <div
            class="border-2 min-h-[2.8rem] border-gray-400 absolute rounded-lg overflow-hidden focus-within:resize focus-within:border-blue-500 p-2 bg-gray-700"
            style="top:{noteBox.y}px; left:{noteBox.x}px; width:{noteBox.width}px; height:{noteBox.height}px;"
            use:resize={[writable(), el => {
                noteBox.width = el.offsetWidth;
                noteBox.height = el.offsetHeight;
            }]}
        >
            <textarea
                bind:this={noteBox.el}
                bind:value={noteBox.content}
                on:input={() => debouncedSave(noteBox)}
                placeholder="Type here!"
                class="w-full h-full !outline-0 resize-none bg-gray-700"
            ></textarea>
            <span
                on:click={() => {
                    fetch(`${PUBLIC_API_URL}/notes/${noteBox.id}/`, {
                        method: 'DELETE',
                    }).then(() => {
                        noteBoxes = noteBoxes.filter((_, i) => i !== idx);
                    })
                }}
                class="absolute text-xs top-[-2.5px] right-[0.3px] select-none cursor-pointer text-gray-600 hover:text-red-500 hover:font-bold text-white"
            >
                X
            </span>
        </div>
    {/each}
</div>

