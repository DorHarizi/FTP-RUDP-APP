# Reliable UDP File Transfer Protocol

## Overview

This project introduces a Reliable UDP (RUDP) File Transfer Protocol, engineered to provide a dependable method for file transmission over networks. Leveraging the simplicity of UDP, the protocol incorporates features to ensure the reliable delivery of files, addressing the inherent unreliability of UDP without the overhead of TCP. This implementation is particularly suited for environments where lightweight data transfer or high throughput is critical.
---

## Reliable UDP (RUDP) Protocol

## Background

The Reliable UDP (RUDP) protocol is designed to offer the best of both worlds: the low overhead and high-speed transmission of UDP, coupled with the reliability features typically found in TCP. While UDP is favored for real-time applications due to its non-blocking send and receive operations, it lacks mechanisms for ensuring data integrity, order, and delivery. RUDP addresses these shortcomings, making it an excellent choice for applications that require both efficiency and reliability.

### How RUDP Works

RUDP enhances UDP by incorporating several key features:

- **Sequence Numbers**: Every packet transmitted over RUDP is uniquely identified by a sequence number. This addition allows the receiving end to sort packets in their original order and identify any missing pieces of data.

- **Acknowledgments (ACKs)**: Receivers send back an acknowledgment packet (ACK) for each successfully received packet. These ACKs inform the sender which packets have arrived safely, facilitating the retransmission of lost data.

- **Retransmission of Lost Packets**: RUDP monitors ACKs from the receiver. If a packet doesn't receive an ACK within a specified timeout, it's considered lost and automatically retransmitted.

- **Flow and Congestion Control**: Like TCP, RUDP implements flow control to prevent overwhelming the receiver and congestion control to adapt to network capacity. These mechanisms ensure efficient and fair use of network resources.

### RUDP in This Project

In our file transfer application, RUDP plays a crucial role in ensuring files are transmitted reliably and efficiently between clients and the server. Here's how we've implemented RUDP features:

- **Packet Management**: Files are broken into numbered packets for transmission. Our application tracks these packets, ensuring each piece of the file is sent and acknowledged in order.

- **Handling Lost Data**: The application detects packets that fail to be acknowledged within a certain timeframe, triggering a retransmission to handle potential data loss.

- **Efficiency**: By leveraging RUDP, our application combines UDP's high throughput with the necessary reliability mechanisms, optimizing file transfer performance even over less reliable networks.

### Demonstration

Our application showcases RUDP's effectiveness in real-world scenarios, providing a robust solution for file transfers. Below are resources demonstrating the application in action:

- **Screenshots**: ![Application Screenshot](path/to/screenshot.png)
- **Video Demonstration**: [![Video Demonstration](path/to/video_thumbnail.png)](path/to/video.mp4)

## Implementation

The project is structured into several key components:

- **Sender:** Breaks down files into packets, manages packet transmission, and handles ACKs to ensure all packets are successfully delivered.
- **Receiver:** Listens for incoming packets, checks sequence numbers to assemble the file in order, and sends ACKs for received packets.

### Classes and Functions

- `server_app.py`: Implements the server-side logic, including file upload, download, and deletion functionalities.
- `client_app.py`: Handles client-side operations, such as connecting to the server and initiating file transfers.
- `sender.py` and `receiver.py`: Contain the core logic for sending and receiving files over RUDP.

## Usage

To start the server:

```bash
python server_app.py
```

To run a client:

```bash
python client_app.py
```

## Demonstrations

### Application Screenshots

![Application Screenshot](path/to/screenshot.png)

*Replace `path/to/screenshot.png` with the actual path to your screenshot.*

### Video Demonstration

[![Video Demonstration](path/to/video_thumbnail.png)](path/to/video.mp4)

*Replace `path/to/video_thumbnail.png` and `path/to/video.mp4` with actual paths to your video thumbnail and video file, respectively.*

## Conclusion

This project successfully demonstrates a practical application of RUDP for file transfers, offering a balance between the efficiency of UDP and the reliability of TCP. It stands as a testament to the potential for custom protocols to meet specific network performance and reliability requirements.

---

Remember to replace placeholder paths with actual paths to your project's screenshots and demonstration videos. Hosting these files on a platform like GitHub, YouTube, or a personal website, and linking them in your README, is a common practice.
