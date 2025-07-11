import { useState } from 'react';
import { FiSearch, FiEdit2, FiCheck } from 'react-icons/fi';
import { RiStickyNoteAddLine } from "react-icons/ri";
import { motion } from 'framer-motion';
import useAxiosAuth from '../utils/useAxiosAuth';

export default function ChatSidebar({ 
  onSelectConversation, 
  activeConversationId, 
  conversations, 
  setConversations,
  isLoading 
}) {
  const [searchTerm, setSearchTerm] = useState('');
  const [editingId, setEditingId] = useState(null);
  const [editedName, setEditedName] = useState('');

  const api = useAxiosAuth();

  const handleCreateNewConversation = async () => {
    onSelectConversation(null);
  };

  const filteredConversations = conversations.filter(
    (conv) => conv.title && conv.title.trim() !== '' && conv.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const handleRename = async (id) => {
    try {
      await api.post(`/users/rename-conversation/`, { new_name: editedName, conversation_id: id });
      setConversations((prev) =>
        prev.map((conv) => (conv.conversation_id === id ? { ...conv, title: editedName } : conv))
      );
      setEditingId(null);
      setEditedName('');
    } catch (error) {
      console.error('Rename failed:', error);
    }
  };

  return (
    <div className="w-full h-full bg-gray-800 p-4 border-r border-gray-700 overflow-hidden flex flex-col">
      <div className="mb-4">
        <button
          onClick={handleCreateNewConversation}
          className="flex items-center bg-purple-600 hover:bg-purple-700 p-3 rounded-lg transition-colors text-white w-full cursor-pointer"
        >
          <RiStickyNoteAddLine className="mr-2" />
          New Conversation
        </button>
      </div>

      <div className="mb-4">
        <div className="flex items-center bg-gray-700 rounded-lg px-3 py-2">
          <FiSearch className="text-gray-400 mr-2" />
          <input
            type="text"
            placeholder="Search..."
            className="bg-transparent outline-none text-white w-full"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
      </div>

      <div className="flex-1 overflow-y-auto space-y-2">
        {isLoading ? (
          <div className="flex justify-center py-8">
            <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-purple-500"></div>
          </div>
        ) : filteredConversations.length === 0 ? (
          <div className="text-center py-8 text-gray-400">
            {searchTerm ? 'No conversations found' : 'No conversations yet'}
          </div>
        ) : (
          filteredConversations.map((conv) => {
            const isActive = conv.conversation_id === activeConversationId;
            return (
              <motion.div
                key={conv.conversation_id}
                onClick={() => onSelectConversation(conv.conversation_id)}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                className={`p-3 rounded-lg flex justify-between items-center cursor-pointer transition-colors duration-200
                  ${isActive ? 'border border-purple-500 bg-gray-700' : 'bg-gray-700 hover:bg-gray-600'}`}
              >
                {editingId === conv.conversation_id ? (
                  <>
                    <input
                      value={editedName}
                      onChange={(e) => setEditedName(e.target.value)}
                      className="bg-gray-600 p-1 rounded text-white flex-1 mr-2"
                      autoFocus
                      onKeyDown={(e) => e.key === 'Enter' && handleRename(conv.conversation_id)}
                    />
                    <button onClick={() => handleRename(conv.conversation_id)}>
                      <FiCheck className="text-green-400 cursor-pointer" />
                    </button>
                  </>
                ) : (
                  <>
                    <span className="text-white truncate">{conv.title}</span>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setEditingId(conv.conversation_id);
                        setEditedName(conv.title);
                      }}
                    >
                      <FiEdit2 className="text-purple-400 ml-2 cursor-pointer" />
                    </button>
                  </>
                )}
              </motion.div>
            );
          })
        )}
      </div>
    </div>
  );
}