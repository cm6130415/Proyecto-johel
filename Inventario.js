import React from 'react';
import { games } from '../mock/games';
import { Package } from 'lucide-react';

const Inventory = () => {
  return (
    <section className="container mx-auto px-4 py-12">
      <h1 className="text-3xl font-bold text-center mb-8">Inventario Completo</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {games.map((game) => (
          <div key={game.id} className="bg-white rounded-xl shadow-lg p-6">
            <div className="flex items-center gap-2 mb-4">
              <Package size={24} className="text-blue-600" />
              <h3 className="text-xl font-bold text-gray-800">{game.title}</h3>
            </div>
            <p className="text-gray-600">{game.description}</p>
            <p className="text-gray-500 mt-2">Categoría: {game.category}</p>
            <p className="text-gray-500 mt-2">Stock Total: {game.stock} unidades</p>
            <p
              className={`px-3 py-1 rounded-full text-sm font-medium mt-3 ${
                game.available ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
              }`}
            >
              {game.available ? 'Disponible' : 'Prestado'}
            </p>
          </div>
        ))}
      </div>
      <p className="text-center text-gray-500 mt-8">
        Inventario actualizado en tiempo real por la biblioteca de la Universidad Simón Bolívar.
      </p>
    </section>
  );
};

export default Inventory;