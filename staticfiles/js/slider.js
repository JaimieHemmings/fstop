  // Get the image track element
  const track = document.getElementById("image-track");
  
  // Handle mouse/touch down event
  const handleOnDown = e => track.dataset.mouseDownAt = e.clientX;
  
  // Handle mouse/touch up event
  const handleOnUp = () => {
    // Reset mouse down position
    track.dataset.mouseDownAt = "0";  
    // Store the current percentage position
    track.dataset.prevPercentage = track.dataset.percentage;
  }
  
  // Handle mouse/touch move event
  const handleOnMove = e => {
    // Exit if mouse is not down
    if(track.dataset.mouseDownAt === "0") return;
    
    // Calculate the change in mouse position
    const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
          maxDelta = window.innerWidth / 2;
    
    // Calculate the percentage change based on mouse movement
    const percentage = (mouseDelta / maxDelta) * -100,
          nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
          nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);
    
    // Update the track's percentage position
    track.dataset.percentage = nextPercentage;
    
    // Animate the track's position
    track.animate({
      transform: `translate(${nextPercentage}%, 0%)`
    }, { duration: 1200, fill: "forwards" });
    
    // Animate each image's position within the track
    for(const image of track.getElementsByClassName("image")) {
      image.animate({
        objectPosition: `${100 + nextPercentage}% center`
      }, { duration: 1200, fill: "forwards" });
    }
  }
  
  // Attach event listeners for mouse and touch events
  window.onmousedown = e => handleOnDown(e);
  window.ontouchstart = e => handleOnDown(e.touches[0]);
  window.onmouseup = e => handleOnUp(e);
  window.ontouchend = e => handleOnUp(e.touches[0]);
  window.onmousemove = e => handleOnMove(e);
  window.ontouchmove = e => handleOnMove(e.touches[0]);