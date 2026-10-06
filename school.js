import React from 'react';
import { View, Text, Button } from 'react-native';

const App = () => {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Welcome to My App!</Text>
      <Button title="Go to Home" onPress={() => {}} />
    </View>
  );
};

export default App;
