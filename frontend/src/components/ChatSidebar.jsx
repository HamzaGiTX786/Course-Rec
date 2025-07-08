import { useEffect, useState } from 'react';
import { FiSearch, FiEdit2, FiCheck } from 'react-icons/fi';

import useAxiosAuth from '../utils/useAxiosAuth'; 

export default function ChatSidebar() {
  const [conversations, setConversations] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [editingId, setEditingId] = useState(null);
  const [editedName, setEditedName] = useState('');

  const api = useAxiosAuth();

  // Fetch conversations when the component mounts
  useEffect(() => {
    const fetchConversations = async () => {
      try {
        const res = await api.get('/users/all-conversations/');
        console.log('Fetched conversations:', res.data.data);
        setConversations(res.data.data);
      } catch (error) {
        console.error('Failed to fetch conversations:', error);
      }
    };

    fetchConversations();
  }, []);

  const handleRename = async (id) => {
    try {
      await api.post(`/users/rename-conversation/`, 
        { new_name: editedName,
          conversation_id: id
         });
      setConversations(prev =>
        prev.map(conv => (conv.conversation_id === id ? { ...conv, title: editedName } : conv))
      );
      setEditingId(null);
      setEditedName('');
    } catch (error) {
      console.error('Rename failed:', error);
    }
  };

  const filteredConversations = conversations.filter(conv =>
    conv.title?.toLowerCase().includes(searchTerm.toLowerCase())
  );


  return (
    <div className="w-72 bg-gray-800 p-4 border-r border-gray-700">
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
        {filteredConversations.map((conv) => (
          <div
            key={conv.conversation_id}
            className="bg-gray-700 hover:bg-gray-600 p-3 rounded-lg flex justify-between items-center"
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
                  onClick={() => {
                    setEditingId(conv.conversation_id);
                    setEditedName(conv.title);
                  }}
                >
                  <FiEdit2 className="text-purple-400 ml-2 cursor-pointer" />
                </button>
              </>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
