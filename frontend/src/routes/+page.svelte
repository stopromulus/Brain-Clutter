<script>
    import calendarimage from '$lib/images/calendar-image.png';
    import notesicon from '$lib/images/note-icon.png';
    // import listicon from '$lib/images/list-icon.png';
    import meditationicon from '$lib/images/meditation-icon.png';
    import Iconbutton from './iconbutton.svelte';
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&family=Roboto+Mono:ital,wght@0,700;1,700&display=swap" rel="stylesheet">

<style>
    h1 {
        font-family: 'Roboto Mono', monospace;
    }
    div {
        font-family: 'Poppins', sans-serif;
    }
</style>

<h1 class="text-center text-8xl mb-10 pt-32 pb-20 tracking-tighter">Brain Clutter</h1>

<div class="font-serif">
    <div class="grid grid-cols-3 justify-items-center">
        <Iconbutton name="calendar" src={calendarimage} alt="Calendar icon"></Iconbutton>
        <Iconbutton name="notes" src={notesicon} alt="Notes icon" link="/notes"></Iconbutton>
        <!-- <Iconbutton name="list" src={listicon} alt="List icon"></Iconbutton> -->
        <Iconbutton name="meditation" src={meditationicon} alt="Meditation" link="/meditation"></Iconbutton>
    </div>
</div>
