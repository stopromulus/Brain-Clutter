import { PUBLIC_API_URL } from "$env/static/public";

export const csr = true;
export const ssr = false;


/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
  try {
    return {
      notes: await fetch(`${PUBLIC_API_URL}/notes/`).then(res => res.json()),
    };
  } catch (error) {
    console.error(error);
  }
}
