import React, { useEffect, useRef } from 'react';
import { View, Text, Button } from 'react-native';

export default function HomeScreen() {
  const ws = useRef<WebSocket | null>(null);

  useEffect(() => {
    ws.current = new WebSocket('ws://YOUR_IP:8000/ws/audio');

    ws.current.onopen = () => {
      console.log('Connected to server');
    };

    ws.current.onmessage = (event) => {
      console.log('Received echo:', event.data);
    };

    ws.current.onerror = (error) => {
      console.log('WebSocket error:', error);
    };

    ws.current.onclose = () => {
      console.log('Disconnected');
    };

    return () => {
      ws.current?.close();
    };
  }, []);

  const sendDummyData = () => {
    if (ws.current && ws.current.readyState === WebSocket.OPEN) {
      const randomBytes = new Uint8Array([1, 2, 3, 4, 5]);
      ws.current.send(randomBytes);
      console.log("Sent dummy bytes");
    }
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>WebSocket Test</Text>
      <Button title="Send Dummy Audio" onPress={sendDummyData} />
    </View>
  );
}
