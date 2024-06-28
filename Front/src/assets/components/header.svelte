<script>
  let elmt = ""
  const getCharacter = async () => {
    if(!elmt) {
      return null;
    }
    let response = await fetch (`http://127.0.0.1:8000/api/character/${elmt}`);
    let result = await response.json();
    console.log(response);
    console.log(result);

    return result;
  }
  let characterPromise = getCharacter();
  const onclick = () => {
    characterPromise = getCharacter();
  }
</script>











<header>
  <nav class="flex items-center justify-between flex-wrap bg-[#AE1C1C] p-0">
    <div class="flex items-center flex-shrink-0 text-white mr-6"></div>
    <div class="block lg:hidden"></div>

    <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
      <img class="size-1/12 m-10" src="theboys.png" alt="logo" />
      <div class="flex items-center justify-center mx-32">
        <form>
        <div class="flex w-full mx-0 rounded-md bg-white">
          <input
            id = "name"
            bind:value={elmt}
            class="w-full border-none bg-transparent px-32 py-2 text-gray-400 outline-none focus:outline-none"
            type="search"
            name="q"
            placeholder="Chercher un personnage..."
          />
        </div>
        <button
          type="submit"
          class="m-0 rounded-md bg-[#C1850F] px-32 py-2 text-white"
          on:click|preventDefault={onclick}
        > 
          Rechercher
        </button>
      </form>

      {#await characterPromise}
      <h2>Chargement....</h2>
    {:then character}
        {#if character}
      <h2>Personnage trouvé !<br>{character.character_nickname}</h2>
        {:else}
        <h2>aucun résultat..</h2>
        {/if}
    {:catch err}
      <h2>Erreur lors du chargement de données..</h2>
    {/await}

      </div>
    </div>
  </nav>
</header>
