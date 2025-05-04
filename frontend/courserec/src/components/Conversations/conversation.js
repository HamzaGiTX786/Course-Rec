import urls from "../../shared/url.js";
function AllConversations(){

    // This component will handle all conversations. It will have a list of chat boxes and a search bar.
    // Each chat box will display a conversation between a user and the assistant.
    // The search bar will allow users to search for specific conversations.    

    function getAllConversations(){
        history = fetch(urls.all_conversations, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('accessToken')
            }
        })
    }

    return(
        <nav>
            
        </nav>
    )
}

export default AllConversations;