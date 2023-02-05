<script>
    import calendarimage from '$lib/images/calendar-image.png';
    import notesicon from '$lib/images/note-icon.png';
    // import listicon from '$lib/images/list-icon.png';
    import meditationicon from '$lib/images/meditation-icon.png';
    import Iconbutton from './iconbutton.svelte';
</script>

<h1 class="text-center text-8xl mb-10 underline underline-offset-8 pt-32 pb-20">Brain Clutter</h1>

<div class="font-serif">
    <div class="grid grid-cols-3 justify-items-center">
        <Iconbutton name="calendar" src={calendarimage} alt="Calendar icon"></Iconbutton>
        <Iconbutton name="notes" src={notesicon} alt="Notes icon" link="/notes"></Iconbutton>
        <!-- <Iconbutton name="list" src={listicon} alt="List icon"></Iconbutton> -->
        <Iconbutton name="meditation" src={meditationicon} alt="Meditation" link="/meditation"></Iconbutton>
    </div>
</div>
