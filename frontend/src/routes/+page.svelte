<script>
    import calendarimage from '$lib/images/calendar-image.png';
    import notesicon from '$lib/images/note-icon.png';
    import listicon from '$lib/images/list-icon.png';
</script>

<h1 class="text-center text-2xl">Brain Clutter</h1>

<div class="font-serif">
    <button class="center ml-20">
        <div class=" border-solid border-2">
            Calendar 
            <img src={calendarimage} alt="Calendar Icon" class="w-16">
        </div>
    </button>

    <button class="center">
        <div class="border-solid border-2">
         Notes 
            <img src={notesicon} alt="Notes Icon" class="w-16">
        </div>
    </button>

    <button class="center">
        <div class=" border-solid border-2">
            List 
            <img src={listicon} alt="Notes Icon" class="w-16">
        </div>
    </button> 
</div>