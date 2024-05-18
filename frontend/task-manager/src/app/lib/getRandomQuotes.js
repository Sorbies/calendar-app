export default async function getRandomQuotes(){
    try {
        let response = await fetch("https://zenquotes.io/api/quotes", {next: {revalidate: 3600}});
        let data = await response.json();
        return data;
    } catch (error) {
        console.log(error);
    }

}