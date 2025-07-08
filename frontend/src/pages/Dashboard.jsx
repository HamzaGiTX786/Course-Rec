import { useState } from 'react';
import { motion } from 'framer-motion';
import { FaPaperPlane } from 'react-icons/fa';
import ChatSidebar from '../components/ChatSidebar';

import useAxiosAuth from '../utils/useAxiosAuth'; 

export default function Dashboard() {

  const api = useAxiosAuth();

  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    { sender: 'bot', text: "Hi! I'm CourseRec. Ask me about your courses."}
  ]);
  const [error, setError] = useState(null);
  let res;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');

    try{
    const response = await api.post('/recommend/prompt/', 
      { 
        prompt: input 
      }
    );
     res = response.data;
  } catch (error) {
    console.error('Error sending message:', error);
    }

    if(res.status !== 200) {
    console.error('Error while sending message', res.message);
    setError('Failed to send message. Please try again.');
    return;
  }

   const botResponse = { sender: 'bot', text: `${res.data.message}`};
    setTimeout(() => setMessages((prev) => [...prev, botResponse]), 500);
}

  return (
    <div className="flex min-h-screen bg-gray-900 text-white">
      <ChatSidebar />
      <div className="flex-1 flex flex-col p-4">
        <motion.div 
          initial={{ opacity: 0, y: -10 }} 
          animate={{ opacity: 1, y: 0 }} 
          className="flex-1 overflow-y-auto space-y-4 mb-4 bg-gray-800 p-4 rounded-xl shadow-inner"
        >
            {messages.map((msg, idx) => (
            <motion.div 
                key={idx}
                initial={{ opacity: 0 }} 
                animate={{ opacity: 1 }}
                className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}
            >
                <div className={`p-3 rounded-xl max-w-lg ${msg.sender === 'user' ? 'bg-purple-600' : 'bg-gray-700'}`}>
                {msg.text}
                </div>
            </motion.div>
            ))}
        </motion.div>

        <form onSubmit={handleSubmit} className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={e => setInput(e.target.value)}
            placeholder="Type your question here..."
            className="flex-1 p-3 rounded-lg bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
          />
          <button 
            type="submit"
            className="bg-purple-600 hover:bg-purple-700 p-3 rounded-lg transition-colors"
          >
            <FaPaperPlane />
          </button>
        </form>
      </div>
    </div>
  );
}
