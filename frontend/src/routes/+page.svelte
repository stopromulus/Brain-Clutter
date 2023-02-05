<script>
    import calendarimage from '$lib/images/calendar-image.png';
    import notesicon from '$lib/images/note-icon.png';
    import listicon from '$lib/images/list-icon.png';
    import Iconbutton from './iconbutton.svelte';
</script>

<h1 class="text-center text-2xl mb-10">Brain Clutter</h1>

<div class="font-serif">
    <div class="grid grid-cols-3 justify-items-center">
        <Iconbutton name="calendar" src={calendarimage} alt="Calendar icon"></Iconbutton>
        <Iconbutton name="notes" src={notesicon} alt="Notes icon"></Iconbutton>
        <Iconbutton name="list" src={listicon} alt="List icon"></Iconbutton>
    </div>
</div>