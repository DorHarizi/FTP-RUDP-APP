---

# Reliable UDP File Transfer Protocol

## Overview

This project introduces a Reliable UDP (RUDP) File Transfer Protocol, engineered to provide a dependable method for file transmission over networks. Leveraging the simplicity of UDP, the protocol incorporates features to ensure the reliable delivery of files, addressing the inherent unreliability of UDP without the overhead of TCP. This implementation is particularly suited for environments where lightweight data transfer or high throughput is critical.

## Custom Protocol Description

Our RUDP protocol introduces two main features to enhance reliability over UDP:

- **Sequence Numbering:** Each packet is assigned a unique sequence number, ensuring that data can be reassembled in the correct order despite the unordered nature of UDP.
- **Acknowledgments (ACKs):** Receivers send back an acknowledgment for each packet received. Senders use these ACKs to verify delivery and resend packets as necessary.

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
