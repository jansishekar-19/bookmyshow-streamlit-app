import streamlit as st
import qrcode, io, random
from datetime import datetime
from reportlab.pdfgen import canvas

st.set_page_config(page_title="BookMyShow Style")
st.title("🎬 BookMyShow Style Movie Booking")
movies={"Interstellar":"https://via.placeholder.com/300x450?text=Interstellar","Inception":"https://via.placeholder.com/300x450?text=Inception"}
movie=st.selectbox('Movie',list(movies.keys()))
st.image(movies[movie],width=180)
name=st.text_input('Customer Name')
seats=st.multiselect('Seats',[f'A{i}' for i in range(1,41)])
price=200*len(seats)
st.write(f'Total: ₹{price}')
if st.button('Book') and seats:
    bid='MOV'+datetime.now().strftime('%Y%m%d%H%M%S')
    qr=qrcode.make(bid)
    st.image(qr,caption='QR Ticket')
    pdf='ticket.pdf'
    c=canvas.Canvas(pdf)
    c.drawString(100,800,'Movie Ticket')
    c.drawString(100,780,f'Booking ID: {bid}')
    c.drawString(100,760,f'Customer: {name}')
    c.drawString(100,740,f'Movie: {movie}')
    c.drawString(100,720,f'Seats: {", ".join(seats)}')
    c.save()
    with open(pdf,'rb') as f:
        st.download_button('Download PDF',f,'ticket.pdf')
