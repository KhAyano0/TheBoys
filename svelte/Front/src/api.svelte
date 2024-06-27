<script lang="js">
  let characters = [];
  let currentError = null;
  const getCharacters = () => {
    const res = fetch(`http://127.0.0.1:8000/api/`)
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log(data);
        if (data) characters = data;
      })
      .catch((error) => {
        currentError = "Error";
        console.log("Error fetching characters", error);
      });
  };
  (function () {
    getCharacters();
  })();
</script>

<div class="flex">
  {#each characters as character (character.character_id)}
    <ul id="card">
      <li class="text-center">
        <img
          class="size-1/2 ml-14 mb-6 mt-8"
          alt="logo_characters"
          src={character.character_image}
        />
        <a href="#/"><p>{character.character_nickname}</p></a>
        <p>{character.character_group}</p>
      </li>
    </ul>
  {:else}
    {#if currentError !== null}
      <p>Failed to load data</p>
    {/if}
  {/each}
  </div>

<style>
  #card {
    margin: 4px;
    width: 250px;
    height: 250px;
    background: rgba(255, 255, 255, 0.5);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(10px);
    border-radius: 8px;
  }
</style>
