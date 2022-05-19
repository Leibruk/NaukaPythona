MAX_VOICE_STAMINA = 100

def create_person(who):
    return {'who': who, 'voice_stamina': MAX_VOICE_STAMINA}

def say(ctx, what: str):
    if ctx['voice_stamina'] == 0:
        raise ValueError("Voice Overhelm")
    ctx['voice_stamina'] = max(0, ctx['voice_stamina'] - 20)
    print(f"{ctx['who']}: {what} (stamina={ctx['voice_stamina']})")


def sing(ctx, what: str):
    if ctx['voice_stamina'] == 0:
        raise ValueError("Voice Overhelm")
    ctx['voice_stamina'] = max(0, ctx['voice_stamina'] - 60)
    print(f"{ctx['who']}: {what.upper()} (Stamina={ctx['voice_stamina']})")
    #decrease stamina

if __name__ == "__main__":
    radek_ctx = create_person("Radek")
    say(radek_ctx, "Hello world!")
    say(radek_ctx, "Hello world!")
    sing(radek_ctx, "O sole mio!")
    zbyszek_ctx = create_person("Zbyszek")
    say(zbyszek_ctx, "Hello world!")