#init mod 
init:
    $ mods["i_died_million_times"]=u"{font=IDMT/fonts/LC Chalk.ttf}{color=#ff2400}Я умерла миллион раз, чтобы ты заметил меня: Redux{/color}{/font}" 

init python: 
    config.archives.append("IDMT/666idmt666")

#globals and variables 
init: 
    $ witchhouse_shake = 0 
    $ witchhouse_musicpos = None 

init python:
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0


#transforms 
init: 
    transform idmt_dizzy(m, t, subpixel=True):
        subpixel subpixel
        parallel:
            xoffset 0
            ease 0.75 * t xoffset 10 * m
            ease 0.75 * t xoffset 5 * m
            ease 0.75 * t xoffset -5 * m
            ease 0.75 * t xoffset -3 * m
            ease 0.75 * t xoffset -10 * m
            ease 0.75 * t xoffset 0
            ease 0.75 * t xoffset 5 * m
            ease 0.75 * t xoffset 0
            repeat
        parallel:
            yoffset 0
            ease 1.0 * t yoffset 5 * m
            ease 2.0 * t yoffset -5 * m
            easein 1.0 * t yoffset 0
            repeat  

    transform idmt_blur: 
        blur 15 
        ease 7.5 blur 4 
        ease 7.5 blur 15 
        repeat 

    transform idmt_fastblur: 
        blur 4
    
    transform idmt_night_filter:
        matrixcolor SaturationMatrix(0.5) * BrightnessMatrix(-0.2) * TintMatrix((85, 105, 185)) 

    transform idmt_bxw_filter: 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1)

    transform idmt_mshake:
        subpixel True
        function idmt_modshake 

    transform idmt_dvplicate: 
        mesh True 
        shader "witchhouse.duplicate" 
        u_speed 1.0
        easeout 5.0 u_speed 5.0

    transform idmt_mvtrix: 
        mesh True 
        shader "witchhouse.matrix" 
        u_resolution (1920, 1080) 
        u_mouse (960, 540) 


    transform idmt_oldcinema: 
        mesh True 
        shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080) 
        u_mouse (960, 540, 0) 


    transform idmt_bloodlake: 
        mesh True 
        shader "witchhouse.bloodlake" 
        yzoom -1 
        u_bloodlevel 0.38 
        block: 
            ease 2.5 u_bloodlevel 0.41 
            ease 2.5 u_bloodlevel 0.38 
            repeat

    transform idmt_blvrred: 
        mesh True 
        shader "witchhouse.blurred" 
        u_resolution (1920, 1080) 
        u_mouse (960, 540) 

#filters
init python: 
    def idmt_bloodypict(img): 
        return im.MatrixColor(ImageReference(img), im.matrix.brightness(0.4) * im.matrix.contrast(3.5) * im.matrix.colorize("#ff0000", "#000000")) 

    def idmt_darkpict(img): 
        return im.MatrixColor(ImageReference(img), im.matrix.brightness(0.2) * im.matrix.contrast(3.5) * im.matrix.colorize("#111111", "#000000")) 

    def idmt_burneyespict(img): 
        return im.MatrixColor(ImageReference(img), im.matrix.brightness(0) * im.matrix.contrast(3.5) * im.matrix.colorize("#aaaaaa", "#0000ff"))


#effects
init python: 

    def idmt_modshake(trans, st, at): 
        global witchhouse_shake
        
        import random
        
        trans.xoffset = random.uniform(-witchhouse_shake, witchhouse_shake)
        trans.yoffset = random.uniform(-witchhouse_shake, witchhouse_shake)
        
        return 0.0 

    def idmt_randomStart(disp, xsize=0): 
        import random 
        disp = renpy.displayable(disp)
        cut_fract = random.randint(0, xsize) / float(xsize)
        first_part = Transform(disp, crop_relative=True, crop=(0.0, 0.0, cut_fract, 1.0))
        second_part = Transform(disp, crop_relative=True, crop=(cut_fract, 0.0, 1.0, 1.0))
        return HBox(second_part, first_part) 

    def screenshot_srf():
        srf = renpy.display.draw.screenshot(None)
        
        return srf 

    def hide_windows_enabled(enabled=True):
        global _windows_hidden
        _windows_hidden = not enabled

    class idmt_TearPiece:
        def __init__(self, startY, endY, offtimeMult, ontimeMult, offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax
        
        def update(self, st):
            st = st % (self.offTime + self.onTime)
            if st > self.offTime and self.offset == 0:
                self.offset = random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0

    class idmt_Tear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf=None):
            super(idmt_Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            if float(self.width) / float(self.height) > 16.0/9.0:
                self.width = self.height * 16 / 9
            else:
                self.height = self.width * 9 / 16
            self.number = number
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf
            self.pieces = []
            tearpoints = [0, self.height]
            for i in range(number):
                tearpoints.append(random.randint(10, self.height - 10))
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(idmt_TearPiece(tearpoints[i], tearpoints[i+1], offtimeMult, ontimeMult, offsetMin, offsetMax))
        
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.blit(self.srf, (0,0))
            for piece in self.pieces:
                piece.update(st)
                subsrf = self.srf.subsurface((0, max(0, piece.startY - 1), self.width, max(0, piece.endY - piece.startY)))
                render.blit(subsrf, (piece.offset, piece.startY))
            renpy.redraw(self, 0)
            return render

screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None):
    zorder 150
    add idmt_Tear(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size (1920,1080)
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action Function(hide_windows_enabled, enabled=True) 


init python:
    class idmt_Blood(object):
        def __init__(self, theDisplayable, density=120.0, particleTime=1.0, dripChance=0.05, dripSpeedX=0.0, dripSpeedY=120.0, dripTime=180.0, burstSize=100, burstSpeedX=200.0, burstSpeedY=400.0, numSquirts=4, squirtPower=400, squirtTime=0.25):
            self.sm = SpriteManager(update=self.update)
            self.drops = []
            self.squirts = []
            self.displayable = theDisplayable
            self.density = density
            self.particleTime = particleTime
            self.dripChance = dripChance
            self.dripSpeedX = dripSpeedX
            self.dripSpeedY = dripSpeedY
            self.gravity = 800.0
            self.dripTime = dripTime
            self.burstSize = burstSize
            self.burstSpeedX = burstSpeedX
            self.burstSpeedY = burstSpeedY
            self.lastUpdate = 0
            self.delta = 0.0
            
            for i in range(burstSize): self.add_burst(theDisplayable, 0)
            for i in range(numSquirts): self.add_squirt(squirtPower, squirtTime)
        
        def add_squirt(self, squirtPower, squirtTime):
            angle = random.random() * 6.283
            xSpeed = squirtPower * math.cos(angle)
            ySpeed = squirtPower * math.sin(angle)
            self.squirts.append([xSpeed, ySpeed, squirtTime])
        
        def add_burst(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.burstSpeedX + 20
            ySpeed = (random.random() - 0.75) * self.burstSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])
        
        def add_drip(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.dripSpeedX + 20
            ySpeed = random.random() * self.dripSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])
        
        def update(self, st):
            delta = st - self.lastUpdate
            self.delta += st - self.lastUpdate
            self.lastUpdate = st
            
            sindex = 0
            for xSpeed, ySpeed, squirtTime in self.squirts:
                if st > squirtTime: self.squirts.pop(sindex)
                sindex += 1
            
            pindex = 0
            if st < self.dripTime:
                while self.delta * self.density >= 1.0:
                    self.delta -= (1.0 / self.density)
                    if random.random() >= 1 - self.dripChance: self.add_drip(self.displayable, st)
                    for xSpeed, ySpeed, squirtTime in self.squirts:
                        s = self.sm.create(self.displayable)
                        s.x += (random.random() - 0.5) * 5
                        s.y += (random.random() - 0.5) * 5
                        self.drops.append([s, xSpeed + (random.random() - 0.5) * 20, ySpeed + (random.random() - 0.5) * 20, self.particleTime, st])
            for s, xSpeed, ySpeed, particleTime, startTime in self.drops:
                if (st - startTime < particleTime):
                    s.x += xSpeed * delta
                    s.y += ySpeed * delta
                    self.drops[pindex][2] += self.gravity * delta
                else:
                    s.destroy()
                    self.drops.pop(pindex)
                pindex += 1
            return 0 

init python: 
    class idmt_RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0  

init python:

    class idmt_LumaMask(renpy.display.layout.Container):
        def __init__(self, child, mask, **properties):
            super(idmt_LumaMask, self).__init__(**properties)
            
            self.mask = renpy.easy.displayable(mask)
            self.add(self.mask)
            self.add(child)
        
        def render(self, width, height, st, at):
            cr = renpy.display.render.render(self.child, width, height, st, at)
            w, h = cr.get_size()
            
            mr = renpy.display.render.Render(w, h)
            mr.place(self.mask, main=False)
            
            rv = renpy.display.render.Render(w, h, opaque=False)
            
            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = 1.0
            rv.operation_complete = 256.0 / (256.0 + 256.0)
            rv.operation_parameter = 256
            
            rv.mesh = True
            rv.add_shader("witchhouse.mask")
            rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)
            
            rv.blit(mr, (0, 0))
            rv.blit(cr, (0, 0))
            
            self.offsets = [ (0, 0), (0, 0) ]
            
            return rv 

init python:    
    from renpy.display.transform import polar_to_cartesian
    
    class Vector(renpy.object.Object):
        """
        It's honestly stolen.
        """
        def __init__(self, *data):
            self.data = data
            
        def __repr__(self):
            return repr(self.data) 
            
        def __add__(self, other):
            return tuple((a+b for a,b in zip(self.data, other.data)))
            
        def __sub__(self, other):
            return tuple((a-b for a,b in zip(self.data, other.data)))
            
    class SingleParticle(renpy.object.Object):
        """
        Class of one particle
        """
        def __init__(self, sp, fp, t, rt, ft, zoom, alpha, st):
            self.start_pos = sp 
            self.finish_pos = fp
            
            self.part_time = t
            self.rise_time = rt 
            self.fall_time = ft 
            
            self.max_zoom = zoom 
            self.max_alpha = alpha
            
            self.oldst = st
            self.pos = self.start_pos 
            self.zoom = .0
            self.alpha = .0
            
    class CustomParticles(renpy.Displayable):   
        from random import randint, uniform
        from math import sqrt, pow
        
        def __init__(self, part_img, parts_count=300):
            super(CustomParticles, self).__init__()
            self.part_img = renpy.displayable(part_img)
            
            self.w, self.h = (config.screen_width, config.screen_height)
            
            #self.max_parts = parts_count
            self.particles = [self.make_particle() for i in xrange(parts_count)]
            
        def get_rand_cord(self, w, h):
            """
            Returninig of random coordinate within the limits w, h
            """
            return self.randint(-100, w+100), self.randint(-100, h+100)
            
        def progress_calc(self, oldst, t, st):
            target = oldst + t 
            anim_time = target - st 
            res = 1.0 - anim_time / t
            
            if res < .0:
                return .0
            elif .0 <= res <= 1.0:
                return res 
            else:
                return 1.0
            
        def make_particle(self, st=float()):
            """
            Particle creation. Returning of object SingleParticle
            """
            w, h, = self.w, self.h 
            
            start_pos = self.get_rand_cord(w, h)
            finish_pos = self.get_rand_cord(w, h)
            xdist, ydist = Vector(*finish_pos) - Vector(*start_pos)
            
            speed = self.uniform(90, 110)
            
            part_time = self.sqrt(self.pow(xdist, 2) + self.pow(ydist, 2)) / speed
            rise_time = part_time * self.uniform(.1, .25)
            fall_time = part_time * self.uniform(.1, .25)
            
            
            max_alpha = self.uniform(.25, .75)
            max_zoom = self.uniform(.25, .75)
            
            part = SingleParticle(start_pos,
                                  finish_pos,
                                  part_time,
                                  rise_time,
                                  fall_time,
                                  max_zoom,
                                  max_alpha,
                                  st)
            return part
            
        def update_particle(self, part_idx, st):
            part = self.particles[part_idx]
            
            t = part.part_time 
            rt = part.rise_time
            ft = part.fall_time 
            
            start_time = part.oldst
            rise_time = start_time + rt
            fall_time = start_time + t - ft
            
            anim_progress = self.progress_calc(start_time, t, st)
            rise_progress = self.progress_calc(rise_time, rt, st)
            fall_progress = self.progress_calc(fall_time, ft, st)
            
            rise_vs_fall = rise_progress - fall_progress
            
            part.pos = renpy.atl.interpolate(anim_progress,
                                             part.start_pos,
                                             part.finish_pos,
                                             (int, int))
            
            part.alpha = part.max_alpha * rise_vs_fall
            part.zoom = part.max_zoom * rise_vs_fall
            
            if anim_progress >= 1.0:
                self.particles.pop(part_idx)
                self.particles.append(self.make_particle(st))
            
            
        
        def visit(self):
            return [self.part_img for i in self.particles]
            
        def render(self, w, h, st, at):
            rv = renpy.Render(w, h)
            
            for idx, part in enumerate(self.particles):
                self.update_particle(idx, st)
                xpos, ypos = part.pos
                
                if 0 < xpos < w and 0 < ypos < h:
                    t = Transform(child=self.part_img, 
                                  alpha=part.alpha,
                                  zoom=part.zoom)
                
                    #Use blit for optimization
                    tr = t.render(w, h, st, at)
                    rv.blit(tr, (xpos, ypos))
                
            renpy.redraw(self, .0)
            return rv 

init python: 
    import math 
    import builtins 
    class idmt_AnimatedMask(renpy.Displayable):    
        def __init__(self, child, mask, maskb, oc, op, moving=True, speed=1.0, frequency=1.0, amount=0.5, **properties):
            super(idmt_AnimatedMask, self).__init__(**properties)            
            self.child = renpy.displayable(child)
            self.mask = renpy.displayable(mask)
            self.maskb = renpy.displayable(maskb)
            self.oc = oc
            self.op = op
            self.null = None
            self.size = None
            self.moving = moving
            self.speed = speed
            self.amount = amount
            self.frequency = frequency
        def render(self, width, height, st, at):            
            cr = renpy.render(self.child, width, height, st, at)
            mr = renpy.render(self.mask, width, height, st, at)
            mb = renpy.Render(width, height)            
            if self.moving:
                mb.place(self.mask, ((-st * 50) % (width * 2)) - (width * 2), 0)
                mb.place(self.maskb, -width / 2, 0)
            else:
                mb.place(self.mask, 0, 0)
                mb.place(self.maskb, 0, 0)            
            cw, ch = cr.get_size()
            mw, mh = mr.get_size()            
            w = builtins.min(cw, mw)
            h = builtins.min(ch, mh)
            size = (w, h)            
            if self.size != size:
                self.null = Null(w, h)            
            nr = renpy.render(self.null, width, height, st, at)            
            rv = renpy.Render(w, h, opaque=False)            
            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = 1.0
            rv.operation_complete = self.oc + math.pow(math.sin(st * self.speed / 8), 64 * self.frequency) * self.amount
            rv.operation_parameter = self.op 
            if renpy.display.render.models: 
                target = rv.get_size() 
                if self.op < 1:
                    self.op = 1 
                start = -1.0
                end = self.op / 256.0
                offset = start + (end - start) * rv.operation_complete 
                rv.mesh = True
                rv.add_shader("renpy.imagedissolve",)
                rv.add_uniform("u_renpy_dissolve_offset", offset)
                rv.add_uniform("u_renpy_dissolve_multiplier", 256.0 / self.op)
                rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap) 
            rv.blit(mb, (0, 0), focus=False, main=False)
            rv.blit(nr, (0, 0), focus=False, main=False)
            rv.blit(cr, (0, 0))            
            renpy.redraw(self, 0)
            return rv
