import { createStore } from 'redux';

const initialState = {
  user: null,
  history: [],
};

function reducer(state = initialState, action) {
  switch (action.type) {
    case 'LOGIN':
      return { ...state, user: action.payload };
    case 'ADD_HISTORY':
      return { ...state, history: [...state.history, action.payload] };
    case 'CLEAR_HISTORY':
      return { ...state, history: [] };
    default:
      return state;
  }
}

const store = createStore(reducer);

export default store;
