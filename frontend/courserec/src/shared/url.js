domain = "http://localhost:8000/"

urls = {
    login: domain + 'users/login',
    create: domain + 'users/create',
    user: domain + 'user/',
    refresh: domain + 'users/refresh',
    prompt: domain + 'recommend/prompt',
    logout: domain + '/logout',
    all_conversations: domain + 'users/all-conversations',
}

export default urls;