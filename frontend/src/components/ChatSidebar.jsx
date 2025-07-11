import { useState } from 'react';
import { FiSearch, FiEdit2, FiCheck } from 'react-icons/fi';
import { RiStickyNoteAddLine } from "react-icons/ri";

import useAxiosAuth from '../utils/useAxiosAuth';

export default function ChatSidebar({ onSelectConversation, activeConversationId, conversations, setConversations }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [editingId, setEditingId] = useState(null);
  const [editedName, setEditedName] = useState('');

  const api = useAxiosAuth();

  const handleCreateNewConversation = async () => {
    onSelectConversation(null); // Reset active conversation
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
    <div className="w-72 bg-gray-800 p-4 border-r border-gray-700">
      <div className="mb-4">
        <button
          onClick={handleCreateNewConversation}
          className="flex items-center bg-purple-600 hover:bg-purple-700 p-3 rounded-lg transition-colors text-white w-full cursor-pointer"
        >
          <RiStickyNoteAddLine  className="mr-2" />
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

      <div className="space-y-2 overflow-y-auto max-h-[calc(100vh-120px)]">
        {filteredConversations.map((conv) => {
          const isActive = conv.conversation_id === activeConversationId;
          return (
            <div
              key={conv.conversation_id}
              onClick={() => onSelectConversation(conv.conversation_id)}
              className={`p-3 rounded-lg flex justify-between items-center cursor-pointer transition-colors duration-200
                ${isActive ? 'border border-purple-500 bg-gray-700' : 'bg-gray-700 hover:bg-gray-600'}`}
            >
              {editingId === conv.conversation_id ? (
                <>
                  <input
                    value={editedName}
                    onChange={(e) => setEditedName(e.target.value)}
                    className="bg-gray-600 p-1 rounded text-white flex-1 mr-2"
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
            </div>
          );
        })}
      </div>
    </div>
  );
}
