import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { FaPaperPlane } from 'react-icons/fa';
import ChatSidebar from '../components/ChatSidebar';

import useAxiosAuth from '../utils/useAxiosAuth';
import { useAuth } from '../utils/AuthProvider'; 

export default function Dashboard() {
  const navigate = useNavigate();
  const api = useAxiosAuth();
  const { logout } = useAuth();

  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [error, setError] = useState(null);
  const [activeConversationId, setActiveConversationId] = useState(null);
  const [isTyping, setIsTyping] = useState(false);
  const [conversations, setConversations] = useState([]); // Store conversations here

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const fetchConversations = async () => {
    try {
      const res = await api.get('/users/all-conversations/');
      setConversations(res.data.data); // Update conversations list from backend
    } catch (error) {
      console.error('Failed to fetch conversations:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsTyping(true);

    try {
      const response = await api.post('/recommend/prompt/', {
        prompt: input,
        conversation_id: activeConversationId || null
      });

      if (response.status !== 200) {
        setError('Failed to send message. Please try again.');
        setIsTyping(false);
        return;
      }

      const { data, conversation_id } = response.data || {};

      if (!data) {
        setError('No response message from server.');
        setIsTyping(false);
        return;
      }

      // Update conversation ID if it was just created
      if (!activeConversationId && conversation_id) {
        setActiveConversationId(conversation_id);
        fetchConversations(); // Update the conversation list after a new one is created
      }

      const botResponse = { sender: 'bot', text: data };
      setMessages((prev) => [...prev, botResponse]);
    } catch (error) {
      console.error('Error sending message:', error);
      setError('Failed to send message. Please try again.');
    } finally {
      setIsTyping(false);
    }
  };

  const handleConversationSelect = async (conversationId) => {
    if (conversationId) {
    try {
      setActiveConversationId(conversationId);

      const response = await api.post('/users/conversation/', {
        conversation_id: conversationId
      });

      const conversationData = response.data.data;

      const convMessages = conversationData.flatMap((entry) => ([
        { sender: 'user', text: entry.prompt },
        { sender: 'bot', text: entry.completion }
      ]));

      setMessages(convMessages);
    } 
     catch (error) {
      console.error('Failed to load conversation messages:', error);
      setMessages([{ sender: 'bot', text: "Failed to load conversation. Try again." }]);
    }
  }else{
      setActiveConversationId(null);
      setMessages([]); // Clear messages if no conversation is selected
    }
  };

  useEffect(() => {
    fetchConversations(); // Fetch conversations when the component mounts
  }, []);

  return (
    <div className="flex min-h-screen bg-gray-900 text-white">
      <ChatSidebar 
        onSelectConversation={handleConversationSelect}
        activeConversationId={activeConversationId}
        conversations={conversations}  // Pass conversations to the sidebar
        setConversations={setConversations} // Provide method to update the list of conversations
      />
      <div className="flex-1 flex flex-col p-4">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-2xl font-bold">Dashboard</h1>
          <button
            onClick={handleLogout}
            className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded-lg transition-colors cursor-pointer"
            type="button"
          >
            Logout
          </button>
        </div>

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
              <div
                className={`p-3 rounded-xl max-w-lg ${msg.sender === 'user' ? 'bg-purple-600' : 'bg-gray-700'}`}
              >
                {msg.text}
              </div>
            </motion.div>
          ))}

          {isTyping && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex justify-start"
            >
              <div className="p-3 rounded-xl max-w-lg bg-gray-700 italic text-gray-300 animate-pulse">
                CourseRec is typing...
              </div>
            </motion.div>
          )}
        </motion.div>

        <form onSubmit={handleSubmit} className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
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
