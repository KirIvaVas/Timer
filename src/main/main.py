import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer


main_frame_width = 500  # 440
main_frame_height = 600  # 350
pad_evr = 10
font_size = 12
ent_place_height = round(font_size*1.3*6)

num = [str(i) if i >= 10 else '0' + str(i) for i in range(60)]



def description():
    ent = ttk.Label(root,
                    text="DESCRIPTION:\n"
                         "Interval traning. Use slides to adjust suitable "
                         "time.\n"
                         "\"START\" button for start count.\n"
                         "\"STOP\" button for a stop.\n",
                    font=("Arial", font_size),
                    )
    ent.place(height=ent_place_height,
              width=main_frame_width-pad_evr*2,
              x=pad_evr,
              y=pad_evr
              )


def rep_frame():
    frame = ttk.Frame(borderwidth=0,
                      relief="ridge",
                      padding=[pad_evr, pad_evr])
    desc = ttk.Label(frame,
                    text="Choose the number of repetitions.",
                    font=("Arial", 12, "bold"),
                    )

    desc.pack(anchor="nw", fill="x")
    global rpttns
    rpttns = tk.Scale(frame,
                      orient="horizontal",
                      tickinterval=1,
                      from_=1,
                      to=9,
                      variable=reps,
                      state="active",
                      takefocus=1
                      )
    rpttns.pack(anchor="nw", fill="x")
    frame.place(width=main_frame_width-pad_evr*2,
          x=pad_evr,
          y=rep_place_height
          )


def timer_frames():
    global wtm, wts, rtm, rts
    frame_wt = ttk.Frame(borderwidth=0,
                         relief="ridge",
                         padding=[pad_evr, pad_evr]
                         )

    for c in range(5): frame_wt.columnconfigure(index=c, weight=1)
    for r in range(3): frame_wt.rowconfigure(index=r, weight=1)

    # Working time general
    ttk.Label(frame_wt,
              text="Working time:",
              font=("Arial", 12, "bold")
              )\
        .grid(column=0, row=0, columnspan=2, sticky="nw")

    # Working time minutes
    ttk.Label(frame_wt,
              text="minutes:",
              font=("Arial", 12,)
              )\
        .grid(column=0, row=1, sticky="nw")

    wtm = ttk.Combobox(frame_wt, textvariable=w_min, values=num,
                          width=6, justify="center", state="readonly")
    wtm.grid(column=0, row=2, sticky="nw")

    # Working time seconds
    ttk.Label(frame_wt,
              text="seconds:",
              font=("Arial", 12,)
              ) \
        .grid(column=1, row=1, sticky="nw")


    wts = ttk.Combobox(frame_wt, textvariable=w_sec, values=num,
                          width=6, justify="center", state="readonly")
    wts.grid(column=1, row=2, sticky="nw")

    # Rest time general
    ttk.Label(frame_wt,
              text="Rest time:",
              font=("Arial", 12, "bold")
              )\
        .grid(column=3, row=0, columnspan=2, sticky="nw")

    # Rest time minutes
    ttk.Label(frame_wt,
              text="minutes:",
              font=("Arial", 12,)
              )\
        .grid(column=3, row=1, sticky="nw")

    rtm = ttk.Combobox(frame_wt,
                       textvariable=r_min,
                       values=num,
                       width=6,
                       justify="center",
                       state="readonly"
                       )
    rtm.grid(column=3, row=2, sticky="nw")

    # Rest time seconds
    tk.Label(frame_wt,
              text="seconds:",
              font=("Arial", 12,)
             ) \
        .grid(column=4, row=1, sticky="nw")

    rts = ttk.Combobox(frame_wt,
                       textvariable=r_sec,
                       values=num,
                       width=6,
                       justify="center",
                       state="readonly"
                       )
    rts.grid(column=4, row=2, sticky="nw")


    frame_wt.place(width=main_frame_width - pad_evr * 2,
                   x=pad_evr,
                   y=240
                   )


def play_sound(sound):
    file = f"../../data/static/{sound}.wav"
    # load the sound file
    sound = mixer.Sound(file)
    # play the sound
    sound.play()
    # wait for the sound to finish
    while mixer.get_busy():
        pass


def status_frame():
    frame = ttk.Frame(borderwidth=0,
                      relief="ridge",
                      padding=[pad_evr, pad_evr]
                      )

    frame.columnconfigure(index=0, weight=3)
    frame.columnconfigure(index=1, weight=4)
    frame.columnconfigure(index=2, weight=0)
    frame.columnconfigure(index=3, weight=1)
    frame.columnconfigure(index=4, weight=3)
    for v in range(3): frame.rowconfigure(index=v, weight=0)


    # Rep status
    reps_label_name = ttk.Label(frame,
              text="Number of reps: ",
              font=("Arial", 12),
              )
    reps_label_name.grid(column=0, row=0, sticky="e")
    reps_label_num = ttk.Label(frame,
              textvariable=reps,
              font=("Arial", 12, "bold"),
              )
    reps_label_num.grid(column=1, row=0, pady=5)
    global left_reps_label
    left_reps_label = ttk.Label(frame,
                               text="0",
                               font=("Arial", 24, "bold"),
                               )
    left_reps_label.grid(column=8, row=0, columnspan=13, pady=5)


    def work_rest_status(name, row_num, min, sec):
        """
        Work/Rest lables and data.
        :param name: Status name of progressbar.
        :param row_num: Row position number.
        :param min: Time in minutes.
        :param sec: Time in seconds
        :return:
        """
        work_label_name = ttk.Label(frame,
                  text=name,
                  font=("Arial", 12),
                  )
        work_label_name.grid(column=0, row=row_num, sticky="e", pady=10)
        work_label_min = ttk.Label(frame,
                  textvariable=min,
                  font=("Arial", 12, "bold"),
                  )
        work_label_min.grid(column=4, row=row_num, sticky="e", pady=10)
        ttk.Label(frame,
                  text=":",
                  font=("Arial", 12, "bold")
                  ).grid(column=6, row=row_num)
        work_label_sec = ttk.Label(frame,
                                   textvariable=sec,
                                   font=("Arial", 12, "bold"),
                                   )
        work_label_sec.grid(column=7, row=row_num, sticky="e", pady=10)



    # Work status
    work_rest_status("Work: ", 1, w_min, w_sec)

    # Work progressbar
    global work_pb
    work_pb = ttk.Progressbar(frame,
        orient='horizontal',
        mode='determinate',
        length=240,
        value=0,
        maximum=0
        )
    work_pb.grid(column=8, row=1, padx=pad_evr, pady=10)

    # Rest status
    work_rest_status("Rest: ", 2, r_min, r_sec)

    # Work progressbar
    global rest_pb
    rest_pb = ttk.Progressbar(frame,
        orient='horizontal',
        mode='determinate',
        length=240,
        value=0,
        maximum=0
        )
    rest_pb.grid(column=8, row=2, padx=pad_evr, pady=10)

    frame.place(width=main_frame_width - pad_evr * 2,
                x=pad_evr,
                y=410
                )


def buttons_frames():
    # is_running = True

    def stop_status():
        global is_running
        is_running = False
        rpttns.config(state="active", takefocus=0)
        wtm.config(state="readonly")
        wts.config(state="readonly")
        rtm.config(state="readonly")
        rts.config(state="readonly")
        start_button.config(state="active")
        stop_button.config(state="disabled")
        left_reps_label['text'] = "0"

        work_pb['value'] = 0
        rest_pb['value'] = 0
        root.update()

    def update_progress(work_rest_status, reps_var):
        if not is_running or reps_var <= 0:
            stop_status()
            play_sound("finish")
            return
        else:
            if work_rest_status == rest_pb \
                    and work_rest_status['value'] == work_rest_status['maximum']:
                reps_var -= 1
                left_reps_label['text'] = reps_var
                work_pb['value'] = 0
                rest_pb['value'] = 0
                root.update()
                if reps_var > 0:
                    play_sound("start")
                update_progress(work_pb, reps_var)
            elif work_rest_status == rest_pb:
                work_rest_status['value'] += 1
                root.after(1000, update_progress, work_rest_status, reps_var)
            else:
                if work_rest_status['value'] == work_rest_status['maximum']:
                    play_sound("rest")
                    update_progress(rest_pb, reps_var)
                else:

                    work_rest_status['value'] += 1
                    root.after(1000, update_progress, work_rest_status,
                               reps_var)


    def start_status():
        global is_running
        is_running = True
        reps_var = reps.get()
        work_time = int(w_min.get()) * 60 + int(w_sec.get())
        rest_time = int(r_min.get()) * 60 + int(r_sec.get())

        if work_time == 0 or rest_time == 0:
            stop_status()

        rpttns.config(state="disabled", takefocus=0)
        wtm.config(state="disabled")
        wts.config(state="disabled")
        rtm.config(state="disabled")
        rts.config(state="disabled")
        start_button.config(state="disabled")
        stop_button.config(state="active")
        root.update()

        work_pb.config(maximum=work_time)
        rest_pb.config(maximum=rest_time)

        work_pb['value'] = 0
        rest_pb['value'] = 0
        left_reps_label['text'] = reps_var

        play_sound("start")

        # Main cycle
        update_progress(work_pb, reps_var)


    frame = ttk.Frame(borderwidth=0,
                         relief="ridge",
                         padding=[pad_evr, pad_evr]
                      )

    for c in range(2): frame.columnconfigure(index=c, weight=1)
    for r in range(1): frame.rowconfigure(index=r, weight=1)


    # Start button
    global start_button
    start_button = ttk.Button(frame,
               text="Start",
               command=start_status,
               width=20,
               state="active"
               )
    start_button.grid(column=0, row=0,)

    # Stop button
    global stop_button
    stop_button = ttk.Button(frame,
               text="Stop",
               command=stop_status,
               width=20,
               state="disabled"
               )
    stop_button.grid(column=1, row=0,)

    frame.place(width=main_frame_width - pad_evr * 2,
                   x=pad_evr,
                   y=345)


root = tk.Tk()
root.iconphoto(False, tk.PhotoImage(file="../../data/static/icon.png"))
root.title("Interval Training Timer by KirIvaVas")
# initialize the mixer
mixer.init()

reps = tk.IntVar(value=1)
w_min = tk.StringVar(value=num[0])
w_sec = tk.StringVar(value=num[0])
r_min = tk.StringVar(value=num[0])
r_sec = tk.StringVar(value=num[0])

pos_x = int(root.winfo_screenwidth() / 2 - main_frame_width / 2)
pos_y = int(root.winfo_screenheight() / 2 - main_frame_height / 2)
root.wm_attributes("-topmost", 1)
root.geometry(f"{main_frame_width}x{main_frame_height}+{pos_x}+{pos_y}")
root.resizable(False, False)

description()

rep_place_height = ent_place_height + pad_evr * 2

rep_frame()
timer_frames()
status_frame()
buttons_frames()


root.mainloop()
# clean up the mixer
mixer.quit()

if __name__ == "__main__":
    # Do nothing
    pass



